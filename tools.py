# Main code management and loop
import os
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.utilities import WikipediaAPIWrapper
from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()


def init_llm():
    llm=ChatOpenAI(
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    temperature=0,
    model_name='gpt-3.5-turbo')
    
    return llm



'''def create_tools():
    #Wrappers
    wikipedia = WikipediaAPIWrapper()
    search = SerpAPIWrapper()
    llm_math = LLMMathChain(llm=init_llm())
    tools = [
        Tool(
            name="Current Search",
            func=search.run,
            description="useful for when you need to answer questions about current events or the current state of the world."
        ),
        Tool(
            name="wikipedia",
            func=wikipedia.run,
            description="Useful for details about a concept you are not familiar with and need extensive information."
        ),
        Tool(
            name="Calculator",
            func=llm_math.run,
            description="Useful for when you need to answer questions about math"),
        Tool(
        name = "Summary",
        func=summary_chain.run,
        description="useful for when you summarize a conversation. The input to this tool should be a string, representing who will read this summary."
    )]
    

'''