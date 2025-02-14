from typing_extensions import TypedDict, Literal, Annotated
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime
import pandas as pd
from langchain_core.messages import (
    AnyMessage
)
from langgraph.graph import add_messages, MessagesState


class Query(BaseModel):
    """
    Represents an exploration query designed to extract insights from the fantasy football dataset.
    """

    question: str = Field(
        description=(
            "A clear and concise question that specifies the information or insight needed from the dataset. "
            "Example: 'What is the total number of wins for each team across all seasons?'"
        )
    )
    reasoning: str = Field(
        description=(
            "A detailed explanation justifying why the question is important and what insights are expected. "
            "This should include context and any assumptions about the data, e.g., the relevance of home and away games."
        )
    )
    exploration_plan: str = Field(
        description=(
            "A step-by-step plan outlining how to explore the dataset using pandas to answer the question. "
            "Include specific operations, data transformations, and any edge case handling (e.g., data type checks) needed to ensure robustness."
        )
    )

class Result(BaseModel):
    """The result of an exploration of the data set"""

    code: str = Field(description="The code generated to answer the question")
    results: dict = Field(description="The results of the code execution")

class Exploration(BaseModel):
    """An exploration of the data set for more information"""

    query: Query = Field(description="The query to the data set")
    result: Result = Field(description="The result of the query")



class DataAnalysisState(MessagesState):
    '''State for the data analysis agent'''
    dataframe: Optional[pd.DataFrame] = None
    exploration: list[Exploration]
    plan: str
    result: str
    
    
    class Config:
        arbitrary_types_allowed = True


class ConfigSchema(TypedDict):
    thread_id: str


