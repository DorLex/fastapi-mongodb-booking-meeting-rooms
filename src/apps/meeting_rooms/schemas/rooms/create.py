from datetime import datetime, timedelta
from typing import Self

from pydantic import Field, model_validator, field_validator

from src.apps.meeting_rooms.schemas.rooms.base import MeetingRoomBaseSchema


class MeetingRoomInSchema(MeetingRoomBaseSchema):
    booking_start_at: datetime = Field(examples=['2024-06-17 12:00'])
    booking_end_at: datetime = Field(examples=['2024-06-17 13:30'])

    @field_validator('booking_start_at', 'booking_end_at')
    @classmethod
    def validate_minutes(cls, date_time: datetime) -> datetime:
        if date_time.minute not in (0, 30):
            raise ValueError('Минуты могут быть только 00 либо 30')

        return date_time

    @model_validator(mode='after')
    def check_time(self) -> Self:
        if self.booking_start_at >= self.booking_end_at:
            raise ValueError('Время окончания бронирования должно быть больше времени начала')

        if (self.booking_end_at - self.booking_start_at) > timedelta(hours=24):
            raise ValueError('Бронировать можно максимум на 24 часа')

        return self
