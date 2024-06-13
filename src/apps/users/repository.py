from fastapi.security import HTTPBasicCredentials
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.users.models import UserModel


class UserRepository:

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_credentials(self, credentials: HTTPBasicCredentials) -> UserModel:
        hashed_password: str = credentials.password + 'fake_hash'

        query = (
            select(UserModel)
            .where(
                UserModel.username == credentials.username,
                UserModel.password == hashed_password
            )
        )

        return await self._session.scalar(query)
