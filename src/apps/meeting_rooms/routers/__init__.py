from fastapi import APIRouter

from src.apps.meeting_rooms.routers import booking
from src.apps.meeting_rooms.routers import schedule

meeting_rooms_router = APIRouter(
    prefix='/meeting-rooms'
)

meeting_rooms_router.include_router(booking.router)
meeting_rooms_router.include_router(schedule.router)
