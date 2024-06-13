from fastapi import FastAPI

from src.apps.meeting_rooms.routers.local_router import meeting_rooms_router
from src.apps.users.routers.local_router import users_router

app = FastAPI(
    title='Booking Meeting Rooms',
    description='Система для бронирования переговорных комнат',
)

app.include_router(users_router)
app.include_router(meeting_rooms_router)
