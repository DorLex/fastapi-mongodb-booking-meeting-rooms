import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status
from starlette.datastructures import URLPath

from tests.conftest import get_app, get_auth_headers


class TestBookingMeetingRooms:
    app: FastAPI = get_app()
    url: URLPath = app.url_path_for('booking_meeting_room')
    auth_headers: dict = get_auth_headers()
    base_room_data: dict = {
        'title': 'Главная',
        'booking_start_at': '2024-06-17 12:00',
        'booking_end_at': '2024-06-17 13:30'
    }

    async def test_booking_room(self, client: AsyncClient):
        response = await client.post(self.url, json=self.base_room_data, headers=self.auth_headers)
        assert response.status_code == status.HTTP_201_CREATED, response.text

    @pytest.mark.parametrize(
        'room_data',
        [
            base_room_data,
            {
                'title': 'Главная',
                'booking_start_at': '2024-06-17 11:00',
                'booking_end_at': '2024-06-17 12:30'
            },
            {
                'title': 'Главная',
                'booking_start_at': '2024-06-17 13:00',
                'booking_end_at': '2024-06-17 15:00'
            }
        ]
    )
    async def test_booking_occupied_room(self, client: AsyncClient, room_data):
        response = await client.post(self.url, json=room_data, headers=self.auth_headers)
        assert response.status_code == status.HTTP_400_BAD_REQUEST, response.text
