from typing import AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from src.apps.meeting_rooms.repository import MeetingRoomRepository
from src.config import settings
from src.main import app as main_app


@pytest.fixture(scope='session', autouse=True)
async def prepare():
    assert settings.mode == 'TEST'

    yield

    # FIXME: RuntimeError: Event loop is closed
    await MeetingRoomRepository().collection.delete_many({})


def get_app() -> FastAPI:
    return main_app


@pytest.fixture(scope='session')
def app() -> FastAPI:
    return get_app()


@pytest.fixture(scope='session')
async def client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url='http://test') as async_client:
        yield async_client


@pytest.fixture(scope='session')
async def auth_headers() -> dict:
    return {'Authorization': 'Basic YWxleDoxMjM0NTY3ODk='}