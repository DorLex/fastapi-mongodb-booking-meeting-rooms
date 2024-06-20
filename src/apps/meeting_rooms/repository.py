from pprint import pprint

from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase, AsyncIOMotorClient, AsyncIOMotorCursor
from pymongo.results import InsertOneResult

from src.apps.meeting_rooms.schemas.rooms.create import MeetingRoomInSchema
from src.config import settings
from src.databases.mongodb.connection import mongo_client


class MeetingRoomRepository:
    def __init__(self):
        self.client: AsyncIOMotorClient = mongo_client
        self.db: AsyncIOMotorDatabase = self.client[settings.mongo_db_name]
        self.collection: AsyncIOMotorCollection = self.db[settings.mongo_collection_name]

    async def insert_one(self, owner_name: str, meeting_room: MeetingRoomInSchema) -> InsertOneResult:
        data: dict = meeting_room.model_dump()
        data.update({'owner_name': owner_name})

        return await self.collection.insert_one(data)

    async def find_one(self, filters: dict) -> dict:
        return await self.collection.find_one(filters)

    async def check_free_slot(self, meeting_room: MeetingRoomInSchema) -> bool:
        query = {
            'title': meeting_room.title,
            '$or': [
                {'booking_start_at': meeting_room.booking_start_at},

                {'booking_start_at': {'$gt': meeting_room.booking_start_at, '$lt': meeting_room.booking_end_at}},

                {
                    'booking_start_at': {'$lt': meeting_room.booking_start_at},
                    'booking_end_at': {'$gt': meeting_room.booking_start_at},
                },
            ],
        }

        cursor: AsyncIOMotorCursor = self.collection.find(query)
        booked_rooms: list = await cursor.to_list(length=100)

        if booked_rooms:
            return False
        return True
