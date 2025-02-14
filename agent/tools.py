from typing_extensions import Literal
from datetime import datetime, timezone
import asyncio
import logging
from typing import Dict
import pandas as pd
import numpy as np
import os
import traceback

from langchain_core.messages import SystemMessage, HumanMessage, RemoveMessage, AIMessage
from langchain_core.runnables import RunnableConfig

from langgraph.graph import END
from langgraph.graph.message import add_messages
from langgraph.types import Command

from .config import oai_mini, gemini
from .state import (DataAnalysisState, 
                    Exploration, 
                    Query, 
                    Result)
from .prompts import exploration_prompt, initial_context, execute_exploration_prompt

logging.basicConfig(format="%(levelname)s - %(name)s -  %(message)s", level=logging.WARNING)
logging.getLogger("nido").setLevel(logging.INFO)
logger = logging.getLogger("nido")



tools = []
def initialize_data_set(state: DataAnalysisState, config: RunnableConfig) -> DataAnalysisState:
    """Initializes the data set for the analysis."""
    # Get the directory containing the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one directory and locate the CSV file
    csv_path = os.path.join(os.path.dirname(current_dir), 'fantasy_football_history.csv')
    
    state['dataframe'] = pd.read_csv(csv_path)
    return state

def explore_data_set(state: DataAnalysisState, config: RunnableConfig) -> DataAnalysisState:
    """Explores the data set to get a better understanding of the data."""
    try:
    # Explore the data set

        system_message = SystemMessage(content=exploration_prompt.format(initial_context=initial_context))
        updated_messages = [system_message] + state['messages']

        response = gemini.bind_tools([Query], tool_choice="auto").invoke(updated_messages)
        state['messages'] = add_messages(state['messages'], response)
        return state
    except Exception as e:
        logger.error(f"Error in explore_data_set: {str(e)}")
        ai_message = AIMessage(content=f"Error in explore_data_set: {str(e)}")
        state['messages'] = add_messages(state['messages'], ai_message)
        return Command(goto=END)

def should_explore(state: DataAnalysisState, config: RunnableConfig) -> Command[Literal["execute_exploration", "plan_query", END]]:
    """Determines if the data set should be explored further."""
    try:
        message = state['messages'][-1]

        if len(message.tool_calls) == 0:
            return Command(goto="plan_query")
        else:
            if message.tool_calls[0]['name'] == "Query":
                return Command(goto="execute_exploration")
            else:
                return Command(goto=END)
    except Exception as e:

        logger.error(f"Error in route_update: {str(e)}")
        return Command(goto=END)


def execute_exploration(state: DataAnalysisState, config: RunnableConfig) -> DataAnalysisState:
    """Executes the exploration of the data set."""
    # try:
    tool_call = state['messages'][-1].tool_calls[0]
    query = tool_call['args']
    system_message = SystemMessage(content=execute_exploration_prompt.format(context=initial_context))
    human_prompt = (
        """Please generate Python code that uses the existing pandas DataFrame named 'df'. 
        The code should be robust and handle potential data type issues gracefully. 
        For any operations that assume a value is a string (for example, calling `.split()`), first verify the data type and handle cases where the value might be missing or of a different type (e.g., by converting it to a string or defaulting to an empty list). 
        Avoid including any code that reads data from a CSV or file. 
        When you produce your final output, store the results in a dictionary named 'results'. 
        Each key in 'results' should describe the specific output (derived from the exploration plan) and its corresponding value should be the result of that computation. 
        Do not include the DataFrame 'df' directly in the 'results'.
        The code plan is: 
        <code_plan>
        {plan}
        </code_plan>"""
        )
    human_message = HumanMessage(content=human_prompt.format(plan=query["exploration_plan"]))
        
    response = gemini.invoke([system_message] + [human_message])
    code = response.content

    local_vars = {
            "df": state['dataframe'],
            "pd": pd,
            "np": np,
            "results": {}  # This is where the generated code should store its output.
    }
    try:
        if "```python" in code:
            code = code.split("```python")[1].split("```")[0].strip()

        exec(code, local_vars)
        results = f'Code execeuted: {code}\nResults: {local_vars["results"]}'
    except Exception as e:
        logger.error(f"Error in execute_exploration: {str(e)}")
        results = f'Code execeuted: {code}\nResults: {local_vars["results"]}\nError: {str(e)}'
            
    tool_message = [{"role": "tool", "name": tool_call['name'], "content": results, "tool_call_id": tool_call['id']}]
    state['messages'] = add_messages(state['messages'], tool_message)
    return Command(goto="explore_data_set", update={"messages": state['messages']})
    # except Exception as e:
    #     logger.error(f"Error in execute_exploration: {str(e)}")
    #     ai_message = AIMessage(content=f"Error in execute_exploration: {str(e)}")
    #     state['messages'] = add_messages(state['messages'], ai_message)
    #     return Command(goto=END)


def plan_query(state: DataAnalysisState, config: RunnableConfig) -> DataAnalysisState:
    """Plans the query to the data set."""
    # Plan the query to the data set
    # make query plan

    return state

def execute_query(state: DataAnalysisState, config: RunnableConfig) -> DataAnalysisState:
    """Executes the query to the data set."""
    # Execute the query to the data set
    state['dataframe'] = None
    return state