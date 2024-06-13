from fastapi import APIRouter

from src.apps.meeting_rooms.routers.booking import booking_router

meeting_rooms_router = APIRouter(
    prefix='/meeting-rooms'
)

meeting_rooms_router.include_router(booking_router)
