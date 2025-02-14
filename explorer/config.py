from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic

gemini = ChatGoogleGenerativeAI(
    # model="gemini-1.5-pro",
    model="gemini-2.0-flash",
    temperature=0,
    # other params...
)

oai_mini = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=None,
)

oai_o1 = ChatOpenAI(
    model="o1-preview"
)