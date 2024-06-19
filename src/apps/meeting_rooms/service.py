from datetime import datetime

from pymongo.results import InsertOneResult

from src.apps.meeting_rooms.repository import MeetingRoomRepository
from src.common.schemas.insert_one_result import InsertOneResultSchema


class MeetingRoomService:
    def __init__(self):
        self._repository = MeetingRoomRepository()

    async def insert_one(self, document: dict) -> InsertOneResultSchema:
        result: InsertOneResult = await self._repository.insert_one(document)

        return InsertOneResultSchema(
            inserted_id=str(result.inserted_id),
            acknowledged=result.acknowledged
        )

    async def find_one(self, filters: dict) -> dict:
        return await self._repository.find_one(filters)

    async def check_exist_by_datetime(self, date_time: datetime) -> bool:
        return bool(await self._repository.find_one({'date_time': date_time}))
