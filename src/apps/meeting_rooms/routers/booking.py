from fastapi import APIRouter, Depends

from src.apps.meeting_rooms.schemas.rooms.create import MeetingRoomInSchema
from src.apps.meeting_rooms.service import MeetingRoomService

from src.apps.users.models import UserModel
from src.apps.users.services.auth import get_current_user

booking_router = APIRouter(
    prefix='/booking',
    tags=['Booking meeting rooms']
)


@booking_router.post('/')
async def booking_meeting_room(
        meeting_room: MeetingRoomInSchema,
        # current_user: UserModel = Depends(get_current_user)
):
    """Бронировать переговорную комнату"""

    service = MeetingRoomService()

    return str(meeting_room)
