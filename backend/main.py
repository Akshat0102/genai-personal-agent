from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import dotenv

app = FastAPI(title="Gen AI Personal Assistant", version="1.0")

dotenv.load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Gen AI Personal Assistant is running."}
