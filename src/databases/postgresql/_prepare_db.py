from src.apps.users.models import UserModel
from src.databases.postgresql.base_model import Base
from src.databases.postgresql.connection import async_engine, SessionLocal


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def create_first_user():
    async with SessionLocal() as session:
        db_user = UserModel(
            username='user1',
            email='user1@example.com',
            password='123456789' + 'fake_hash'
        )

        session.add(db_user)
        await session.flush()
        await session.commit()

        return db_user
