import os
from typing import AsyncGenerator, Annotated
from pathlib import Path
from auth.models import Base
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from fastapi import Depends
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

dotenv_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=dotenv_path)

SP_USERNAME = os.getenv('SP_USERNAME')
SP_PASSWORD = os.getenv('SP_PASSWORD')
SP_HOST_URL = os.getenv('SP_HOST_URL')

url_object = URL.create(
    "postgresql+asyncpg",
    username=f'{SP_USERNAME}',
    password=f'{SP_PASSWORD}',
    host=f'{SP_HOST_URL}',
    port=5432,
    database="postgres",
)

engine = create_async_engine(url_object)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
    
SessionDep = Annotated[AsyncSession, Depends(get_session)]

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    
