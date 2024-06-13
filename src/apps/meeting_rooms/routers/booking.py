from fastapi import APIRouter

booking_router = APIRouter(
    prefix='/booking',
    tags=['Booking meeting rooms']
)


@booking_router.post('/')
async def booking_meeting_room():
    """Бронировать переговорную комнату"""

    return 0
