from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.config import settings

async_engine = create_async_engine(
    settings.postgresql_url,
    # echo=True
)

SessionLocal = async_sessionmaker(
    async_engine,
    expire_on_commit=False
)
