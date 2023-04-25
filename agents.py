import os
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import tools
from dotenv import load_dotenv

load_dotenv()
#globals
#tools.create_tools()
#llm = tools.init_llm()
llm=ChatOpenAI(
openai_api_key=os.environ.get("OPENAI_API_KEY"),
temperature=0,
model_name='gpt-3.5-turbo')


 #Create the expert
 
def interviewer(instructions, memory=None):
    if memory is None:
        memory = ConversationBufferMemory()
        memory.ai_prefix = "Expert"
        
    template = f"""Instructions: {instructions}
                {{{memory.memory_key}}}
                Founder: {{founder_input}
                Expert:"""   

    prompt = PromptTemplate(input_variables=["history","founder_input"], template=template)

    chain = LLMChain(llm=llm, prompt=prompt, memory=ConversationBufferMemory(), verbose=True)
        
    return chain

#Instruct the expert

def initialize_expert_chain():
    
    expert_template="""
    You are a professional business consultant. You have interviewed the Founder of a Technology Startup Company about their idea. You are highly critical
    Your job is to ask questions about the Founder's idea and provide feedback. You will write your feedback in a list by highest priority. Your feedback
    will then be sent to the Founder and stored. The objective of the conversation is to generate a set of observations about the new business venture.

    ####

    {chat history}

    ###

    Reflect on these interactions

    You should first ask the Founder about their idea. You should then ask the Founder about their business model. 
    You should then ask the Founder about their marketing strategy. One question at a time.

    Indicate new insights by "Insights: ..."
    """

    expert_prompt = PromptTemplate(input_variables=["chat_history"], template=expert_template)
    
    expert_chain = LLMChain(llm=llm, prompt=expert_prompt, verbose=True)
    
    return expert_chain


