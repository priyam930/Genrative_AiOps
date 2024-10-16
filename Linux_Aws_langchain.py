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

