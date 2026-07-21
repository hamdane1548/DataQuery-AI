from loguru import logger
from pydantic_settings import BaseSettings , SettingsConfigDict
import os
from dotenv import load_dotenv
"""
Sa pour load les env d'un manier dynmaier
sons besoin de chauq fois de utilise le os et le dotenv
aussi isole la responsabilite que load dans un suel place
"""
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",env_file_encoding="UTF-8")
    print("model_config",model_config)
    #Connection to DataBase
    DATABASE : str = "data_query"
    MYSQL_USER : str = "app"
    MYSQL_PASSWORD : str = "app123"
    MYSQL_HOST : str = "localhost"
    MYSQL_PORT : int = 3307

    #Api Key Mistral
    MISTRAL_API_KEY : str = "Dc0T7IKoByfsWRJqPRlBMylBakW4y9sX"
    @classmethod
    def load_settings(cls)->"Settings":
            try:
                """
                make the connection with postgresql
                """
                settings = Settings()
                logger.success("Settings loaded successfully",settings)
                return settings
            except (RuntimeError):
                logger.warning("Failed to load settings and make the connection with postgresql "
                               ""
                               "check the credentials")

settings = Settings.load_settings()

