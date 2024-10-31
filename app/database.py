from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGO_DETAILS, DATABASE_NAME
import asyncio

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client[DATABASE_NAME]

async def connect_to_mongo():
    client.get_io_loop = asyncio.get_running_loop()

async def close_mongo_connection():
    client.close()
