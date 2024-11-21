from fastapi import APIRouter, Depends
from pymongo.results import InsertOneResult
from starlette import status

from src.apps.meeting_rooms.schemas.rooms.create import MeetingRoomInSchema
from src.apps.meeting_rooms.service import MeetingRoomService
from src.apps.users.models import UserModel
from src.apps.users.services.auth import get_current_user
from src.common.schemas.insert_one_result import InsertOneResultSchema

booking_router = APIRouter(
    prefix='/booking',
    tags=['Booking meeting rooms']
)


@booking_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=InsertOneResultSchema
)
async def booking_meeting_room(
        meeting_room: MeetingRoomInSchema,
        current_user: UserModel = Depends(get_current_user)
):
    """Бронировать переговорную комнату"""

    service = MeetingRoomService()
    booked_room: InsertOneResult = await service.booking_room(current_user.username, meeting_room)

    return booked_room
