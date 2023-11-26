from pydantic_settings import BaseSettings

# from pydantic.env_settings import SettingsSourceCallable


class Settings(BaseSettings):
    """
    Application configuration settings.

    Values not passed as keyword arguments are read from the environment if
    available.  Environment variables override settings passed in.
    """

    class Config:
        allow_mutation = False
        env_file = ".env"
