import os
import requests
import uvicorn
from typing import Annotated, Dict
from fastapi import FastAPI, Form, Depends
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from pathlib import Path
from database import init_models
from sqlalchemy import text, select
from database import engine, SessionDep, AsyncSession
from auth.models import UserModel
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from auth.schemas import UserCreate, UserBaseSchema


dotenv_path = Path(__file__).parent.parent / '.env'

origins = [
    "http://localhost:5173",
]

load_dotenv(dotenv_path=dotenv_path)
TESTTOKEN = os.getenv('TESTING_APIKEY')
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

async def check_user_exists(user: UserBaseSchema, async_session: SessionDep):
    username_statement = select(UserModel).where(UserModel.username == user.username)
    email_statement = select(UserModel).where(UserModel.email == user.email)

    email_result = await async_session.scalars(email_statement)
    username_result = await async_session.scalars(username_statement)

    user_email = email_result.first()
    user_username = username_result.first()

    if user_email is None and user_username is None:
        return {"status": False, "cause": "User does not exist"}
    elif user_email != None:
        return {"status": True, "cause": "Email already exists"}
    else:
        return {"status": True, "cause": "Username existing"}
    
async def create_user(user: UserBaseSchema, async_session: SessionDep):
    userToModel = UserModel(
        username = user.username,
        passwordHash = user.hashed_password,
        email = user.email,
        active = user.active

    )
    async_session.add(userToModel)
    await async_session.commit()
            
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

@app.post("/register/")
async def register(email: Annotated[str, Form()], password: Annotated[str, Form()], username: Annotated[str, Form()], session: SessionDep):
    
    hashed_password = get_password_hash(password)
    
    user = UserCreate(
        username = username,
        email = email,
        hashed_password = hashed_password,
        active = True
    )

    userExists = await check_user_exists(user, session)
    print(userExists["status"])
    if userExists["status"] == True:
        return False
    else: 
        await create_user(user, session)
    userExists = await check_user_exists(user, session)
    print(userExists["status"])

        

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)