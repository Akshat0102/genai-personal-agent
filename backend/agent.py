import os
from langchain.agents import Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType
from actions import get_weather, get_time, calculate, summarize
from openai import OpenAI


"""OPENAI Client Initialization"""
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


"""Sample Tools for Agent"""
tools = [
    Tool(
        name="get_weather",
        func=get_weather,
        description="Use this to get weather information for a given city. Input should be the city name."
    ),
    Tool(
        name="get_time",
        func=get_time,
        description="Use this to get current time in a city. Input should be the city name."
    ),
    Tool(
        name="calculate",
        func=calculate,
        description="Use this for evaluating math expressions. Input should be a math expression string."
    ),
    Tool(
        name="summarize_text",
        func=summarize,
        description="Summarize the given text."
    ),

]


"""LLM and Agent Initialization"""
llm = ChatOpenAI(
    temperature=0,
    model="gpt-4o-mini"  # Small, fast, cheap for your project
)


agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


def run_agent(query: str):
    """Function to run the agent with given query."""
    return agent.run(query)
