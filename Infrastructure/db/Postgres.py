import psycopg2
from settings import Settings
from loguru import logger
from psycopg2.extensions import connection
import pymysql
settings = Settings()
class PostgressDatabaseConnector:
    _instance : pymysql.connect | None = None
    def __new__(cls, *args, **kwargs):
        if  cls._instance is None:
            print(settings)
            try:
                cls._instance = pymysql.connect(
                    db=settings.DATABASE,
                    user=settings.MYSQL_USER,
                    password=settings.MYSQL_PASSWORD,
                    host=settings.MYSQL_HOST,
                    port=settings.MYSQL_PORT,
                )
                print("Connected to PostgreSQL",cls._instance)
            except RuntimeError as e:
                logger.error(f"Couldn't connect to PostgreSQL: {e}")
            logger.success(f"Connected to PostgreSQL database via url")

        return cls._instance
connection_Postres = PostgressDatabaseConnector()