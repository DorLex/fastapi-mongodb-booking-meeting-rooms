import asyncio
from typing import AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from src.apps.meeting_rooms.repository import MeetingRoomRepository
from src.config import settings
from src.main import app as main_app


@pytest.fixture(scope='session')
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session', autouse=True)
async def prepare(event_loop) -> None:
    if settings.mode == 'TEST' and settings.mongo_db_name == 'test_schedule':
        yield
        await MeetingRoomRepository().collection.delete_many({})
    else:
        raise ValueError(
            f'{(settings.mode == 'TEST')=}, {(settings.mongo_db_name == 'test_schedule')=}'
        )


def get_app() -> FastAPI:
    return main_app


@pytest.fixture(scope='session')
def app() -> FastAPI:
    return get_app()


@pytest.fixture(scope='function')
async def client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url='http://test') as async_client:
        yield async_client


def get_auth_headers() -> dict:
    return {'Authorization': 'Basic dXNlcjE6MTIzNDU2Nzg5'}


@pytest.fixture(scope='session')
async def auth_headers() -> dict:
    return get_auth_headers()
