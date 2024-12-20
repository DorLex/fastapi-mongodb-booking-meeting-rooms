from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from src.databases.postgresql.connection import SessionLocal


async def pg_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
