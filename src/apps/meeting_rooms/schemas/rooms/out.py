from datetime import datetime

from pydantic import Field, model_validator

from src.apps.meeting_rooms.schemas.rooms.base import MeetingRoomBaseSchema


class MeetingRoomOutSchema(MeetingRoomBaseSchema):
    owner_name: str
    booking_start_at: datetime
    booking_end_at: datetime
    oid: str = Field(validation_alias='_id')

    @model_validator(mode='before')
    @classmethod
    def check_datetime_format(cls, data: dict) -> dict:
        data['_id'] = str(data['_id'])
        return data
