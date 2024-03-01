from langchain.agents import AgentExecutor, XMLAgent, tool
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)


@tool
def search(query: str) -> str:
    """Search things about current events."""
    return "32 degrees"


prompt = XMLAgent.get_default_prompt()
print(f"1. default prompt : \n{prompt} ")
# input_variables=['intermediate_steps', 'question', 'tools']
# messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['question', 'tools'],
# template="You are a helpful assistant. Help the user answer any questions.\n\nYou have access to the following tools:\n\n{tools}\n\nIn order to use a tool,# you can use <tool></tool> and <tool_input></tool_input> tags. You will then get back a response
# in the form <observation></observation>\n
# For example, if you have a tool called 'search' that could run a google search, in order to search for the weather in SF you would
# respond:\n\n<tool>search</tool><tool_input>weather in SF</tool_input>\n<observation>64 degrees</observation>\n\nWhen you are done,
# respond with a final answer between <final_answer></final_answer>. For example:\n\n<final_answer>The weather in SF is
# 64 degrees</final_answer>\n\nBegin!\n\nQuestion: {question}")), AIMessagePromptTemplate(prompt=PromptTemplate(input_variables=['intermediate_steps'],
# template='{intermediate_steps}'))]


def convert_intermediate_steps(intermediate_steps):
    log = ""
    for action, observation in intermediate_steps:
        log += (
            f"<tool>{action.tool}</tool><tool_input>{action.tool_input}"
            f"</tool_input><observation>{observation}</observation>"
        )
    return log


# Logic for converting tools to string to go in prompt
def convert_tools(tools) -> list:
    return "\n".join([f"{tool.name}: {tool.description}" for tool in tools])


tool_list = [search]
agent = (
    {
        "question": lambda x: x["question"],
        "intermediate_steps": lambda x: convert_intermediate_steps(
            x["intermediate_steps"]
        ),
    }
    | prompt.partial(tools=convert_tools(tool_list))
    | llm.bind(stop=["</tool_input>", "</final_answer>"])
    | XMLAgent.get_default_output_parser()
)


query = {"question": "whats the weather in New york?"}

agent_executor = AgentExecutor(agent=agent, tools=tool_list, verbose=True)  # type: ignore
result = agent_executor.invoke(query)
print(f"2. Custom XMLAgent :{result}")
# 2. Custom XMLAgent :{'question': 'whats the weather in New york?', 'output': 'The weather in New York is 32 degrees'}

from langchain.agents import create_xml_agent
from langchain import hub

prompt = hub.pull("hwchase17/xml-agent-convo")
print(f"3-1. Hub Prompt : {prompt}")
query.update(
    {
        "tools": convert_tools(tool_list),
        "agent_scratchpad": lambda x: convert_intermediate_steps(x["agent_scratchpad"]),
    }
)
xml_agent = create_xml_agent(llm=llm, tools=tool_list, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tool_list, verbose=True)  # type: ignore
result = agent_executor.invoke(query)
print(f"3. Created XMLAgent :{result}")
# 3. XMLAgent :{'question': 'whats the weather in New york?', 'tools': 'search: search(query: str) -> str - Search things about current events.', 'agent_scratchpad': <function <lambda> at 0x11fd695e0>, 'output': 'The weather in New York is 32 degrees'}
