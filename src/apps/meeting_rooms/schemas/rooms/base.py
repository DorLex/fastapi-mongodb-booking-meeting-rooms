from pydantic import BaseModel

from src.apps.meeting_rooms.enums import MeetingRoomsEnum


class MeetingRoomBaseSchema(BaseModel):
    title: MeetingRoomsEnum
