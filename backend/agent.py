from config import OPENAI_API_KEY
from actions import get_weather, calculate, summarize
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=OPENAI_API_KEY
)


tools = [get_weather, calculate, summarize]

app = create_react_agent(llm, tools)


async def run_agent(user_input: str):

    result = app.invoke({
        "messages": [
            {"role": "user", "content": user_input}
        ]
    })

    final = result["messages"][-1].content
    return final
