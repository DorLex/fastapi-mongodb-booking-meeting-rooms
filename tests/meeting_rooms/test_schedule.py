from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status
from starlette.datastructures import URLPath

from tests.conftest import get_app, get_auth_headers


class TestMeetingRoomsSchedule:
    app: FastAPI = get_app()
    url: URLPath = app.url_path_for('show_meeting_rooms_schedule')
    auth_headers: dict = get_auth_headers()
    room_data: dict = {
        'title': 'Главная',
        'booking_start_at': '2024-06-16 09:00',
        'booking_end_at': '2024-06-16 10:00'
    }

    async def test_show_meeting_rooms_schedule(self, client: AsyncClient):
        create_url: URLPath = self.app.url_path_for('booking_meeting_room')
        create_response = await client.post(create_url, json=self.room_data, headers=self.auth_headers)
        assert create_response.status_code == status.HTTP_201_CREATED, create_response.text

        read_response = await client.get(self.url, params={'start': '2024-06-16 00:00', 'end': '2024-06-17 00:00'})
        assert read_response.status_code == status.HTTP_200_OK, read_response.text

        read_response_json: list[dict] = read_response.json()

        assert len(read_response_json) > 0
        assert read_response_json[0]['title'] == self.room_data['title']
