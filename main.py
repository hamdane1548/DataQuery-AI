from Infrastructure.db.Postgres import PostgressDatabaseConnector
from Infrastructure.Query_faker import queryDb
from AiAgent.ReAct_db import ReAct
from Infrastructure.AgentConf.AgentEnv import AgentEnv
from loguru import logger
def main():
   ReAct.CreatetheAgent()

if __name__ == "__main__":
    main()
