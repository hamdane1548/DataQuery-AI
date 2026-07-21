from loguru import logger
from settings import Settings
class AgentEnv:
    _instance = None
    def __new__(cls, *args, **kwargs):
        settings = Settings()
        if not cls._instance:
            try:
             token : str = settings.MISTRAL_API_KEY
             if not token:
                 logger.error("error when load the Mistral api key")
                 raise
             cls._instance = token
            except RuntimeError as e:
                logger.error(e)
        logger.info(f"load the Mistral api key")
        return cls._instance
apiKey = AgentEnv()

