from pydantic import HttpUrl

from common.settings import Settings


class AppSettings(Settings):
    """
    Application configuration settings
    """

    primary_origin: HttpUrl
    staging_mode: bool = False
    db_name: str
    db_connection_string: str
