from fastapi.security import HTTPBasicCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.users.models import UserModel
from src.apps.users.repository import UserRepository


class UserService:

    def __init__(self, session: AsyncSession):
        self._session = session
        self._repository = UserRepository(self._session)

    async def get_by_credentials(self, credentials: HTTPBasicCredentials) -> UserModel:
        return await self._repository.get_by_credentials(credentials)
