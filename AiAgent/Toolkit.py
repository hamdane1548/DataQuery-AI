from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from Infrastructure.db.Postgres import  PostgressDatabaseConnector
from langchain_mistralai import ChatMistralAI
from langchain_community.utilities import SQLDatabase
from Infrastructure.AgentConf.AgentEnv import AgentEnv
class Toolkit:
    _api_key: str = AgentEnv()
    @classmethod
    def create_toolkit(cls):
        llm = ChatMistralAI( model="mistral-medium-latest",api_key=cls._api_key,temperature=1)
        db = SQLDatabase.from_uri(
            "mysql+pymysql://app:app123@localhost:3307/data_query"
        )
        toolkit = SQLDatabaseToolkit(db=db,llm=llm)
        return toolkit
toolkit = Toolkit.create_toolkit()

