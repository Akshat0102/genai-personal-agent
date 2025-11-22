from config import OPENAI_API_KEY
import datetime
import httpx
import os
from openai import OpenAI
from langchain.tools import tool


client = OpenAI(api_key=OPENAI_API_KEY)

@tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    return f"The weather in {city} is sunny with 25°C."


@tool
def get_time(city: str) -> str:
    """Get the current time for a given city."""
    now = datetime.datetime.now().strftime("%H:%M")
    return f"The current time in {city} is {now}."

@tool
def calculate(expression: str) -> str:
    """Calculate the result of a mathematical expression."""
    try:
        result = eval(expression, {"__builtins__": {}})
        return f"The result of {expression} is {result}."
    except Exception:
        return "Sorry, I couldn't compute that expression."

@tool
def summarize(text: str) -> str:
    """Summarize the given text using OpenAI's GPT-4o-mini model."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "Summarize the user's text concisely."},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message.content
