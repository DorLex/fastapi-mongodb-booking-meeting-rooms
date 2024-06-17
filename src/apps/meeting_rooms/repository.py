from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase, AsyncIOMotorClient
from pymongo.results import InsertOneResult

from src.databases.mongodb.connection import mongo_client


class MeetingRoomRepository:
    def __init__(self):
        self.client: AsyncIOMotorClient = mongo_client
        self.db: AsyncIOMotorDatabase = self.client.schedule
        self.collection: AsyncIOMotorCollection = self.db.meeting_rooms

    async def insert_one(self, document: dict) -> InsertOneResult:
        return await self.collection.insert_one(document)

    async def find_one(self, filters: dict) -> dict:
        return await self.collection.find_one(filters)
