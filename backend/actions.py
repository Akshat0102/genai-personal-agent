from config import OPENAI_API_KEY
import datetime
import httpx
import os
from openai import OpenAI
from langchain.tools import tool


client = OpenAI(api_key=OPENAI_API_KEY)


@tool
def get_weather(location: str):
    """Fetches real live weather for a given location using Open-Meteo API."""

    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1"

    try:
        geo_resp = httpx.get(geo_url, timeout=5.0)
        geo_data = geo_resp.json()

        if "results" not in geo_data:
            return f"Could not find location: {location}"

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&current_weather=true"
        )

        weather_resp = httpx.get(weather_url, timeout=5.0)
        weather_data = weather_resp.json()

        temp = weather_data["current_weather"]["temperature"]
        wind = weather_data["current_weather"]["windspeed"]

        return f"Current weather in {location}: {temp}°C, wind {wind} km/h"

    except Exception as e:
        return f"Error fetching weather: {str(e)}"


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
