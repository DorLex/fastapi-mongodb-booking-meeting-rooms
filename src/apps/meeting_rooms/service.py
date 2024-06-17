from pymongo.results import InsertOneResult

from src.apps.meeting_rooms.repository import MeetingRoomRepository


class MeetingRoomService:
    def __init__(self):
        self._repository = MeetingRoomRepository()

    async def insert_one(self, document: dict) -> InsertOneResult:
        return await self._repository.insert_one(document)

    async def find_one(self, filters: dict) -> dict:
        return await self._repository.find_one(filters)
