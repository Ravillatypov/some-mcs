from os import environ
from typing import Tuple

from pydantic import BaseModel, Field
from pydantic.env_settings import BaseSettings, SettingsSourceCallable


class Auth(BaseModel):
    """Auth settings."""

    is_enabled: bool = True
    fake_user_id: int = 1
    service_token: str = 'some_token'
    jwt_secret: str = 'secret'


class Setting(BaseSettings):
    """Main application settings."""

    env: str = 'local'
    debug: bool = False
    version: str = '0.1.0'

    db_url: str = 'postgres+asyncpg://user:pass@host/db'

    auth: Auth = Field(default_factory=Auth)

    class Config:
        """Setting configuration."""
        env_nested_delimiter = '__'
        secrets_dir = environ.get('SECRET_DIR', '/tmp')
        env_file = environ.get('ENV_FILE', '.env')

        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> Tuple[SettingsSourceCallable, ...]:
            """Priority load setting."""
            return file_secret_settings, env_settings, init_settings,


setting = Setting()
