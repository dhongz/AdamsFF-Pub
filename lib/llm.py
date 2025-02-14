import streamlit as st
import asyncio
from langchain.callbacks.tracers import LangChainTracer
from langsmith import Client
from langchain_core.messages import HumanMessage

from agent.graph import data_analysis_graph
from lib.config import config

def run_graph(question: str):
    """Async function to run the graph"""
    try:
        langsmith_client = Client(
            api_key=config.LANGCHAIN_API_KEY,
            api_url=config.LANGCHAIN_URL,
        )
        tracer = LangChainTracer(
            client=langsmith_client, 
            project_name="fantasy-test"
        )
        compiled_graph = data_analysis_graph.compile()

        initial_state = {
            'messages': [
                HumanMessage(content=question)
            ]
        }

        result = compiled_graph.invoke(initial_state, config={"callbacks": [tracer]})
        return result['messages'][-1].content
    except Exception as e:
        return f"Error running graph: {str(e)}"