from datetime import datetime

from bson import ObjectId
from pydantic import Field, model_validator, field_validator

from src.apps.meeting_rooms.schemas.rooms.base import MeetingRoomBaseSchema


class MeetingRoomOutSchema(MeetingRoomBaseSchema):
    owner_name: str
    booking_start_at: datetime
    booking_end_at: datetime
    oid: str = Field(validation_alias='_id')

    @field_validator('oid', mode='before')
    @classmethod
    def oid_format(cls, value: ObjectId) -> str:
        return str(value)
