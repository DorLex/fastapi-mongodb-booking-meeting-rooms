from src.apps.meeting_rooms.service import MeetingRoomService


async def meeting_room_service() -> MeetingRoomService:
    return MeetingRoomService()
