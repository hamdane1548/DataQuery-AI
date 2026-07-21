from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from loguru import logger
from  langchain_mistralai import ChatMistralAI
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
         mistralAi = ChatMistralAI(
             model="mistral-medium-latest",
             temperature=1,
             api_key=cls._api_key
         )
         chaine = prompts | mistralAi
         result = ""

         for chunk in chaine.stream({"input": "Demon Slayer"}):
             result += chunk.content
         print(result)

agente = ReAct()

            





