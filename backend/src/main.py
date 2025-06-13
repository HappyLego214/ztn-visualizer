import os
import requests
import uvicorn
from typing import Annotated
from fastapi import FastAPI, Form
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from pathlib import Path
from database import init_models
from sqlalchemy import text
from database import engine
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext

dotenv_path = Path(__file__).parent.parent / '.env'

origins = [
    "http://localhost:5174",
]

load_dotenv(dotenv_path=dotenv_path)
TESTTOKEN = os.getenv('TESTING_APIKEY')

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT * FROM USERS"))
        print(result.all())

    url = "https://api.zerotier.com/api/v1/network/a84ac5c10a7e5fd1/member/129d40c7e4"
    headers = {
        'content-type': 'application/json',
        'Authorization': f'token {TESTTOKEN}'
    }

    response = requests.get(url, headers=headers)
    return {"message": f"{response.json()}"}

@app.post("/login/")
async def login(email: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"email;": email, "password": password}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)