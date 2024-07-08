import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    user_name: str = os.getenv('USER_NAME')
    user_email: str = os.getenv('USER_EMAIL')
    user_phone: int = os.getenv('USER_PHONE')


settings = Settings()
