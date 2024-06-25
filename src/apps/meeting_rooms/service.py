from datetime import datetime

from fastapi import HTTPException
from pymongo.results import InsertOneResult
from starlette import status

from src.apps.meeting_rooms.repository import MeetingRoomRepository
from src.apps.meeting_rooms.schemas.rooms.create import MeetingRoomInSchema


class MeetingRoomService:
    def __init__(self):
        self._repository = MeetingRoomRepository()

    async def booking_room(self, owner_name: str, meeting_room: MeetingRoomInSchema) -> InsertOneResult:
        free_slot_exist: bool = await self._repository.check_free_slot(meeting_room)

        if not free_slot_exist:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                'Это время занято!'
            )

        return await self._repository.insert_one(owner_name, meeting_room)

    async def find_one(self, filters: dict) -> dict:
        return await self._repository.find_one(filters)

    async def find_by_datetime(self, start: datetime, end: datetime) -> list[dict]:
        return await self._repository.find_by_datetime(start, end)
