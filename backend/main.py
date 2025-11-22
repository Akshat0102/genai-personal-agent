from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import run_agent


app = FastAPI(
    title="Personal GenAI Assistant",
    description="Backend for a multi-purpose personal AI agent",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
async def root():
    return {"status": "running", "message": "GenAI Assistant Backend Ready"}


@app.post("/chat")
async def chat(request: ChatRequest):
    """Function to handle chat requests"""
    response = await run_agent(request.message)
    return {"reply": response}

