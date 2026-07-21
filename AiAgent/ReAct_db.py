from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
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
         prompts = ChatPromptTemplate([
             ("system","you are a assistane"),
             ("human","give me the subject for {input}")
         ])

         model = ChatMistralAI( model="mistral-medium-latest",
             temperature=1,
             api_key=cls._api_key)
         agent  = create_agent(model=model,tools=toolkit.get_tools())
         query = input("the query")
         result = agent.invoke({
             "messages": [("user", query)]
         })

         print(result["messages"][-1].content)
agente = ReAct()

            





