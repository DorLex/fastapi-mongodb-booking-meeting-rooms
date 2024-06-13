from fastapi import APIRouter, Depends

from src.apps.users.models import UserModel
from src.apps.users.services.auth import get_current_user

booking_router = APIRouter(
    prefix='/booking',
    tags=['Booking meeting rooms']
)


@booking_router.post('/')
async def booking_meeting_room(current_user: UserModel = Depends(get_current_user)):
    """Бронировать переговорную комнату"""

    return 0
