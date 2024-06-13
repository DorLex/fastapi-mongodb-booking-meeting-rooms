from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    mode: str

    @property
    def postgresql_url(self):
        return (
            f'postgresql+asyncpg://'
            f'{self.postgres_user}:'
            f'{self.postgres_password}@'
            f'{self.postgres_host}:'
            f'{self.postgres_port}/'
            f'{self.postgres_db}'
        )

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()
