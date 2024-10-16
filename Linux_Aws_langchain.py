from langchain_community.tools import ShellTool

# Initialize the ShellTool
shell_tool = ShellTool() 

#shell_tool.run({"commands":["useradd priyam"]})


from langchain.llms import OpenAI

# Initialize the OpenAI language model
mymodel = OpenAI(openai_api_key="your_openai_api_key")

from langchain.agents.agent_types import AgentType

#from langchain.agents import load_tools

from langchain.agents import initialize_agent

mycmd_chain = initialize_agent(llm=mymodel, tools=[shell_tool], agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)

mypromt =  input("Enter Into AI World: ")

output = mycmd_chain.run(mypromt)

print("------------------------------")

print(output)

from langchain_community.tools import ShellTool  # Correct tool import
from langchain.llms import OpenAI  # Correct OpenAI import
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType

# Initialize the ShellTool
shell_tool = ShellTool()

# Initialize the OpenAI language model
mymodel = OpenAI(openai_api_key="your_openai_api_key")

# Initialize the agent using the ShellTool and OpenAI model
mycmd_chain = initialize_agent(
    llm=mymodel,
    tools=[shell_tool],
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Updated agent type
    verbose=True
)

# Take input from user
myprompt = input("Enter Into AI World: ")

# Run the chain with the provided prompt
output = mycmd_chain.run(myprompt)

# Print the result
print("------------------------------")
print(output)
