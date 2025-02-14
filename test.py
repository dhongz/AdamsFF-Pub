from agent.graph import data_analysis_graph
from explorer.graph import explorer_graph
from langchain_core.messages import HumanMessage
import asyncio
from langchain.callbacks.tracers import LangChainTracer
from langsmith import Client
from lib.config import config



async def main():
    langsmith_client = Client(
    api_key=config.LANGCHAIN_API_KEY,
    api_url=config.LANGCHAIN_URL,
)
    tracer = LangChainTracer(
        client=langsmith_client, 
        project_name="fantasy-test"
    )
    compiled_graph = data_analysis_graph.compile()
    compiled_explorer_graph = explorer_graph.compile()

    # initial_state = {
    #     'messages': [
    #         HumanMessage(content="WHo has the most wins?")
    #     ]

    # }

    # result = await compiled_graph.ainvoke(initial_state, config={"callbacks": [tracer]})
    # print(result)
    initial_state = {
        'messages': [
        ]
    }
    result = await compiled_explorer_graph.ainvoke(initial_state, config={"callbacks": [tracer], 'recursion_limit': 50})
    print(result)
if __name__ == "__main__":
    asyncio.run(main())