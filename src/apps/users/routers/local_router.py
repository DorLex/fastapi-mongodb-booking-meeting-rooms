from fastapi import APIRouter

from src.apps.users.routers.auth import auth_router

users_router = APIRouter(
    prefix='/users'
)

users_router.include_router(auth_router)
