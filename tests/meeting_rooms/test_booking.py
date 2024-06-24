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
            base_room_data,  # дубликат слота бронирования комнаты
            {
                'title': 'Главная',
                'booking_start_at': '2024-06-17 11:00',
                'booking_end_at': '2024-06-17 12:30'  # пересечение времени окончания
            },
            {
                'title': 'Главная',
                'booking_start_at': '2024-06-17 13:00',  # пересечение времени начала
                'booking_end_at': '2024-06-17 15:00'
            }
        ]
    )
    async def test_booking_occupied_room(self, client: AsyncClient, room_data: dict):
        response = await client.post(self.url, json=room_data, headers=self.auth_headers)
        assert response.status_code == status.HTTP_400_BAD_REQUEST, response.text

    async def test_booking_room_incorrect_name(self, client: AsyncClient):
        room_data = {
            'title': 'Неправильное название комнаты',
            'booking_start_at': '2024-06-17 01:00',
            'booking_end_at': '2024-06-17 02:00'
        }

        response = await client.post(self.url, json=room_data, headers=self.auth_headers)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.text

    @pytest.mark.parametrize(
        'room_data',
        [
            {
                'title': 'Главная',
                'booking_start_at': '01:00 18.06.2024',  # неверный шаблон datetime
                'booking_end_at': '02:00 18.06.2024'
            },
            {
                'title': 'Главная',
                'booking_start_at': '2024-06-18 01:07',  # неверный шаблон минут
                'booking_end_at': '2024-06-20 02:15'
            },
            {
                'title': 'Главная',
                'booking_start_at': '2024-06-17 01:00',  # одинаковое время начала и конца
                'booking_end_at': '2024-06-17 01:00'
            },
            {
                'title': 'Главная',
                'booking_start_at': '2024-06-17 03:00',  # время начала бронирования > время конца
                'booking_end_at': '2024-06-17 01:00'
            },
            {
                'title': 'Главная',
                'booking_start_at': '2024-06-18 01:00',  # бронирование больше 24 часов
                'booking_end_at': '2024-06-19 01:30'
            },
            {
                'title': 'Главная',
                'booking_start_at': '2024-06-18 01:00',  # бронирование больше 24 часов
                'booking_end_at': '2024-06-20 01:00'
            },
        ]
    )
    async def test_booking_room_incorrect_time(self, client: AsyncClient, room_data: dict):
        response = await client.post(self.url, json=room_data, headers=self.auth_headers)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.text
