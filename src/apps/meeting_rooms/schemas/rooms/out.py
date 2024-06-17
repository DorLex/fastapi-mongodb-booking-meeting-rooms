from datetime import datetime

from src.apps.meeting_rooms.schemas.rooms.base import MeetingRoomBaseSchema


class MeetingRoomOutSchema(MeetingRoomBaseSchema):
    owner_name: str
    booking_start_at: datetime
    booking_end_at: datetime
