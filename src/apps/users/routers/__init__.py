from fastapi import APIRouter
from src.apps.users.routers import auth

users_router = APIRouter(
    prefix='/users'
)

users_router.include_router(auth.router)
