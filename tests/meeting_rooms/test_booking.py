from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status


async def test_booking_meeting_room(app: FastAPI, client: AsyncClient, auth_headers: dict):
    url = app.url_path_for('booking_meeting_room')

    data = {
        'title': 'Главная',
        'booking_start_at': '2024-06-17 12:00',
        'booking_end_at': '2024-06-17 13:30'
    }

    response = await client.post(url, json=data, headers=auth_headers)

    assert response.status_code == status.HTTP_201_CREATED, response.text
