from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.apps.users.dependencies import basic_auth
from src.apps.users.models import UserModel
from src.apps.users.services.user import UserService
from src.databases.postgresql.dependencies import pg_session


async def get_current_user(
        credentials: HTTPBasicCredentials = Depends(basic_auth),
        session: AsyncSession = Depends(pg_session)
) -> UserModel:
    db_user: UserModel = await UserService(session).get_by_credentials(credentials)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Неверный логин или пароль',
            headers={'WWW-Authenticate': 'Basic'},
        )

    return db_user
