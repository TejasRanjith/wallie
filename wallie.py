from langchain import Ollama, LLMChain
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.tools import DuckDuckGoSearchRun

# Initialize the Ollama LLM
llm = Ollama(model="llama2") 

# Initialize a search tool
search = DuckDuckGoSearchRun()

# Create a tool for searching
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    )
]

# Initialize an agent with the LLM and tools
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Run the agent
agent.run("What is the current weather in New York City?")

# how to connect local llama model to internet using python
