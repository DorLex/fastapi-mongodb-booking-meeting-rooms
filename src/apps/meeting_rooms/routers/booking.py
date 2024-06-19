from datetime import datetime

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

    in_db = {
        'booking_start_at': datetime(2024, 6, 17, 12, 0),
        'booking_end_at': datetime(2024, 6, 17, 13, 0)
    }

    if in_db['booking_start_at'] == meeting_room.booking_start_at:
        return 'Нашли, значит занято'

    elif (
            in_db['booking_start_at'] > meeting_room.booking_start_at
            and
            in_db['booking_start_at'] < meeting_room.booking_end_at
    ):
        return 'Нашли, значит занято'

    elif (
            in_db['booking_start_at'] < meeting_room.booking_start_at
            and
            in_db['booking_end_at'] > meeting_room.booking_start_at
    ):
        return 'Нашли, значит занято'

    return 'Не нашли, значит можно создавать новую запись'
