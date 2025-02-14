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
            "A clear and concise question that specifies the information needed to help describe the dataset. "
        )
    )
    reasoning: str = Field(
        description=(
            "A detailed explanation justifying why you are exploring the dataset in this way. "
        )
    )
    exploration_plan: str = Field(
        description=(
            "A detailed step-by-step plan outlining the query you want to run to help describe the dataset "
            "Include specific operations, data transformations, and any edge case handling (e.g., data type checks) needed to ensure robustness."
        )
    )

class Finish(BaseModel):
    """The final dataset description when exploration is complete"""

    description: str = Field(description="The final dataset description in full details")
    additional_columns: str = Field(description="Any additional columns that would be helpful to know about the dataset to help answer queries")
class Result(BaseModel):
    """The result of an exploration   of the data set"""

    code: str = Field(description="The code generated to answer the question")
    results: dict = Field(description="The results of the code execution")

class Exploration(BaseModel):
    """An exploration of the data set for more information"""

    query: Query = Field(description="The query to the data set")
    result: Result = Field(description="The result of the query")



class DataAnalysisState(MessagesState):
    '''State for the data analysis agent'''
    dataframe: Optional[pd.DataFrame] = None
    dataset_description: str
    exploration: list[Exploration]
    plan: str
    result: str
    
    
    class Config:
        arbitrary_types_allowed = True


class ConfigSchema(TypedDict):
    thread_id: str


