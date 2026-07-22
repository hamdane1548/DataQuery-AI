from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from dotenv import load_dotenv
from loguru import logger
from  langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent
from AiAgent.Toolkit import toolkit
import os
from Infrastructure.AgentConf.AgentEnv import AgentEnv
class ReAct():
     _api_key : str = AgentEnv()
     @classmethod
     def CreatetheAgent(cls):
         prompts = ChatPromptTemplate.from_messages([
             ("system","you are a assistane DataBase answer with emojie is possibe"),
             ("human","{input}")
         ])
         not_execute = ["DROP","DELETE","INSERT"]
         model = ChatMistralAI( model="mistral-medium-latest",
             temperature=1,
             api_key=cls._api_key,
            )
         agent  = create_agent(
             model=model,
             tools=toolkit.get_tools(),
         )
         query = input("the query")
         prompts_user = query.split(" ")
         for i in prompts_user:
             if i in not_execute:
                 continue
             else:
                 raise Exception("the prompt should not be executed")
         message = prompts.invoke({"input":query})
         response = agent.invoke({
             "messages":message.to_messages(),
         })

         print(response["messages"][-1].content)
agente = ReAct()

            





