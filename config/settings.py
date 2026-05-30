"""Settings.py file."""

from decouple import AutoConfig

env_config = AutoConfig()

class Config:
    """_summary_."""

    # Database
    DB_NAME = env_config("DB_NAME")
    DB_USER = env_config("DB_USER")
    DB_PASSWORD = env_config("DB_PASSWORD")
    DB_HOST = env_config("DB_HOST")
    DB_PORT = env_config("DB_PORT")