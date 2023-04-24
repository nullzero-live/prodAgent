from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
import tools

#globals
tools.create_tools()
llm = tools.init_llm()

    
#Prioritization
def prior_func():
    priorities = []
    if priorities == []:
        pass


#Task creation

def tasks(query):
    template = """You are a project manager and effective. You are building a business marketing case. You take an objective and break it into steps. A maximum of 10. You will write them in a list by highest priority:

    {chat_history}

    Write a summary of the conversation for {input}:
    """

    prompt = PromptTemplate(
        input_variables=["input", "chat_history"], 
        template=template
    )
    memory = ConversationBufferMemory(memory_key="chat_history")
    readonlymemory = ReadOnlySharedMemory(memory=memory)
    summary_chain = LLMChain(
        llm=llm, 
        prompt=prompt, 
        verbose=True, 
        memory=readonlymemory, # use the read-only memory to prevent the tool from modifying the memory
    )
    
    prefix = """Build a tasklist. Be concise You have access to the following tools:"""
    suffix = """Begin!"

    {chat_history}
    Question: {input}
    {agent_scratchpad}"""

    prompt = ZeroShotAgent.create_prompt(
        tools, 
        prefix=prefix, 
        suffix=suffix, 
        input_variables=["input", "chat_history", "agent_scratchpad"]
    )
    
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
    agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=memory)
    
    return agent_chain.run(input={query})
    

#Search agent
def search_agent(query):
    self_ask_with_search = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)
    
    return self_ask_with_search.run({query})

#context agent
def context(query):
    memory = ConversationBufferMemory(memory_key="chat_history")
    exec_agent = initialize_agent(tools, llm, agent=AgentType.AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)
    
    return exec_agent.run(input={query})

