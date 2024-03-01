from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
query: dict = {"input": "How many letters in the word eudca"}
print(llm.invoke(query.get("input")))

from langchain.agents import tool


# Define tool
@tool
def get_word_length(word: str) -> int:
    """Return the length of a word."""
    return len(word)


tools = {"get_word_length": get_word_length}

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Create promopt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are very powerful assistant, but don't know current events"),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# Bind tools in the llm
llm = llm.bind_tools(list(tools.values()))

from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser

# Define agent
agent = (
    {
        "input": lambda x: x.get("input"),
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm
    | OpenAIToolsAgentOutputParser()
)

from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=list(tools.values()), verbose=True)

result = agent_executor.invoke(query)
print(f"1. invoke : \n{result}\n{type(result)}")
result = list(agent_executor.stream(query))
print(f"2. stream list : \n{result}")

from langchain.schema import AgentFinish, AgentAction
from typing import Union

intermediate_steps = []
final_result = dict()
while True:
    query.update({"intermediate_steps": intermediate_steps})
    output: Union[AgentFinish, AgentAction] = agent.invoke(query)

    if isinstance(output, AgentFinish):
        final_result = output.return_values
        final_result = final_result.get("output")
        break
    else:
        if isinstance(output, list):
            output = output[0]
        print("TOOL NAME : ", output.tool)
        print("TOOL INPUT : ", output.tool_input)
        _tool = tools.get(output.tool)
        observation = _tool.run(output.tool_input)
        intermediate_steps.append((output, observation))

print(f"3. Custom executor : {final_result}")
