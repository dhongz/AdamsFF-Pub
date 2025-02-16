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
                    Dataset,
                    QueryPlan)
from .prompts import exploration_prompt, execute_exploration_prompt, regular_season_context, playoff_context, player_stats_context, matchups_context, query_planner_prompt

logging.basicConfig(format="%(levelname)s - %(name)s -  %(message)s", level=logging.WARNING)
logging.getLogger("nido").setLevel(logging.INFO)
logger = logging.getLogger("nido")


current_dir = os.path.dirname(os.path.abspath(__file__))

tools = []

def explore_data_set(state: DataAnalysisState, config: RunnableConfig) -> DataAnalysisState:
    """Explores the data set to get a better understanding of the data."""
    try:
    # Explore the data set

        system_message = SystemMessage(content=exploration_prompt)
        updated_messages = [system_message] + state['messages']

        response = gemini.bind_tools([Dataset]).invoke(updated_messages)
        state['supervisor_message'] = response
        return state
    except Exception as e:
        logger.error(f"Error in explore_data_set: {str(e)}")
        ai_message = AIMessage(content=f"Error in explore_data_set: {str(e)}")
        state['messages'] = add_messages(state['messages'], ai_message)
        return Command(goto=END)

def should_explore(state: DataAnalysisState, config: RunnableConfig) -> Command[Literal["regular_season_exploration", "playoff_exploration", "player_stats_exploration", "matchups_exploration", "plan_query", END]]:
    """Determines if the data set should be explored further."""
    try:
        message = state['supervisor_message']

        if len(message.tool_calls) == 0:
            state['messages'] = add_messages(state['messages'], message)
            return Command(goto="plan_query", update={"messages": state['messages']})
        
        tool_call = message.tool_calls[0]
        if tool_call['args']['type'] == "RegularSeason":
            return Command(goto="regular_season_exploration")
        elif tool_call['args']['type'] == "Playoff":
            return Command(goto="playoff_exploration")
        elif tool_call['args']['type'] == "PlayerStats":
            return Command(goto="player_stats_exploration")
        elif tool_call['args']['type'] == "Matchups":
            return Command(goto="matchups_exploration")
        else:
            return Command(goto=END)
    except Exception as e:
        logger.error(f"Error in route_update: {str(e)}")
        return Command(goto=END)


def regular_season_exploration(state: DataAnalysisState, config: RunnableConfig) -> DataAnalysisState:
    """Explores the regular season data set."""
    try:
        csv_path = os.path.join(os.path.dirname(current_dir), 'regular_season_totals.csv')
        state['dataframe'] = pd.read_csv(csv_path)
        state['context'] = regular_season_context
        system_message = SystemMessage(content=query_planner_prompt.format(context=regular_season_context))
        updated_messages = [system_message] + state['messages']
        response = gemini.bind_tools([QueryPlan], tool_choice="any").invoke(updated_messages)
        state['messages'] = add_messages(state['messages'], response)
        return Command(goto="execute_exploration", update={"messages": state['messages'], "context": regular_season_context, "dataframe": state['dataframe']})
    except Exception as e:
        logger.error(f"Error in explore_data_set: {str(e)}")
        ai_message = AIMessage(content=f"Error in explore_data_set: {str(e)}")
        state['messages'] = add_messages(state['messages'], ai_message)
        return Command(goto=END)

def playoff_exploration(state: DataAnalysisState, config: RunnableConfig) -> DataAnalysisState:
    """Explores the playoff data set."""
    try:
        csv_path = os.path.join(os.path.dirname(current_dir), 'playoff_totals.csv')
        state['dataframe'] = pd.read_csv(csv_path)
        state['context'] = playoff_context
        system_message = SystemMessage(content=query_planner_prompt.format(context=playoff_context))
        updated_messages = [system_message] + state['messages']
        response = gemini.bind_tools([QueryPlan], tool_choice="any").invoke(updated_messages)
        state['messages'] = add_messages(state['messages'], response)
        return Command(goto="execute_exploration", update={"messages": state['messages'], "context": playoff_context, "dataframe": state['dataframe']})
    except Exception as e:
        logger.error(f"Error in playoff_exploration: {str(e)}")
        ai_message = AIMessage(content=f"Error in playoff_exploration: {str(e)}")
        state['messages'] = add_messages(state['messages'], ai_message)
        return Command(goto=END)    

def player_stats_exploration(state: DataAnalysisState, config: RunnableConfig) -> DataAnalysisState:
    """Explores the player stats data set."""
    try:
        csv_path = os.path.join(os.path.dirname(current_dir), 'player_stats.csv')
        state['dataframe'] = pd.read_csv(csv_path)
        state['context'] = player_stats_context
        system_message = SystemMessage(content=query_planner_prompt.format(context=player_stats_context))
        updated_messages = [system_message] + state['messages']
        response = gemini.bind_tools([QueryPlan], tool_choice="any").invoke(updated_messages)
        state['messages'] = add_messages(state['messages'], response)
        return Command(goto="execute_exploration", update={"messages": state['messages'], "context": player_stats_context, "dataframe": state['dataframe']})
    except Exception as e:
        logger.error(f"Error in player_stats_exploration: {str(e)}")
        ai_message = AIMessage(content=f"Error in player_stats_exploration: {str(e)}")
        state['messages'] = add_messages(state['messages'], ai_message)
        return Command(goto=END)

def matchups_exploration(state: DataAnalysisState, config: RunnableConfig) -> DataAnalysisState:
    """Explores the matchups data set."""
    try:
        csv_path = os.path.join(os.path.dirname(current_dir), 'matchups.csv')
        state['dataframe'] = pd.read_csv(csv_path)
        state['context'] = matchups_context
        system_message = SystemMessage(content=query_planner_prompt.format(context=matchups_context))
        updated_messages = [system_message] + state['messages']
        response = gemini.bind_tools([QueryPlan], tool_choice="any").invoke(updated_messages)
        state['messages'] = add_messages(state['messages'], response)
        return Command(goto="execute_exploration", update={"messages": state['messages'], "context": matchups_context, "dataframe": state['dataframe']})
    except Exception as e:
        logger.error(f"Error in matchups_exploration: {str(e)}")
        ai_message = AIMessage(content=f"Error in matchups_exploration: {str(e)}")
        state['messages'] = add_messages(state['messages'], ai_message)
        return Command(goto=END)





def execute_exploration(state: DataAnalysisState, config: RunnableConfig) -> DataAnalysisState:
    """Executes the exploration of the data set."""
    # try:
    tool_call = state['messages'][-1].tool_calls[0]
    query = tool_call['args']
    system_message = SystemMessage(content=execute_exploration_prompt.format(context=state['context']))
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