import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.ext.asyncio import create_async_engine

dotenv_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=dotenv_path)

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
TESTTOKEN = os.getenv('TESTING_APIKEY')

url_object = URL.create(
    "postgresql+asyncpg",
    username=f'{DB_USERNAME}',
    password=f'{DB_PASSWORD}',
    host="localhost",
    port=5432,
    database="ztn_visualizer_db",
)


engine = create_async_engine(url_object)