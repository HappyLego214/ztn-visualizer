import os
import requests
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import text
from database import engine

dotenv_path = Path(__file__).parent.parent / '.env'
app = FastAPI()

load_dotenv(dotenv_path=dotenv_path)
TESTTOKEN = os.getenv('TESTING_APIKEY')

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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)