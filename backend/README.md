# Backend for GenAI Personal Agent

This is the backend for the GenAI Personal Agent, a multi-purpose personal AI assistant. The backend is built using Python and provides endpoints for interacting with the AI agent.

## Features
- **AI Agent**: Powered by OpenAI's GPT models.
- **Tools Integration**: Includes tools for weather updates, time retrieval, mathematical calculations, and text summarization.
- **FastAPI Framework**: Provides a RESTful API for communication.

## Project Structure
```
backend/
├── .env                # Environment variables
├── .gitignore          # Git ignore file
├── actions.py          # Tool definitions for the AI agent
├── agent.py            # AI agent setup and invocation
├── config.py           # Centralized environment variable loading
├── main.py             # FastAPI application
├── requirements.txt    # Python dependencies
└── __pycache__/        # Compiled Python files
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Akshat0102/genai-personal-agent.git
   cd genai-personal-agent/backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the `.env` file:
   Create a `.env` file in the `backend` directory with the following content:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. Access the API documentation at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

3. Example Endpoints:
   - **Health Check**: `GET /health`
   - **Chat with the Agent**: `POST /chat` with a JSON payload:
     ```json
     {
       "message": "Plan a 3-day trip to Paris, including sightseeing and dining options."
     }
     ```

## Tools
The backend includes the following tools for the AI agent:
- **get_weather(city: str)**: Returns the weather for a given city.
- **calculate(expression: str)**: Evaluates a mathematical expression.
- **summarize(text: str)**: Summarizes the given text using OpenAI's GPT model.

## Dependencies
- `fastapi`
- `uvicorn`
- `python-dotenv`
- `langchain`
- `langchain-openai`
- `langgraph`