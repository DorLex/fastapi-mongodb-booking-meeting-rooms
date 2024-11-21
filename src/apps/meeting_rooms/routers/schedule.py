from datetime import datetime

from fastapi import APIRouter, Query

from src.apps.meeting_rooms.schemas.rooms.out import MeetingRoomOutSchema
from src.apps.meeting_rooms.service import MeetingRoomService

router = APIRouter(
    prefix='/schedule',
    tags=['Meeting rooms schedule']
)


@router.get(
    '',
    response_model=list[MeetingRoomOutSchema]
)
async def show_meeting_rooms_schedule(
        start: datetime = Query(example='2024-06-17 00:00'),
        end: datetime = Query(example='2024-06-18 00:00')
):
    schedule: list[dict] = await MeetingRoomService().find_by_datetime(start, end)
    return schedule
