from motor.motor_asyncio import AsyncIOMotorClient

from src.config import settings

mongo_client = AsyncIOMotorClient(settings.mongodb_url)
