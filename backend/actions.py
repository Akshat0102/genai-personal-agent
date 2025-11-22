import datetime
import httpx
import os
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny with 25°C."


def get_time(city: str) -> str:
    now = datetime.datetime.now().strftime("%H:%M")
    return f"The current time in {city} is {now}."


def calculate(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}})
        return f"The result of {expression} is {result}."
    except Exception:
        return "Sorry, I couldn't compute that expression."


def summarize(text: str) -> str:
    """Function to summarize text using OpenAI's GPT-4o-mini model."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "Summarize the user's text concisely."},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message["content"]
