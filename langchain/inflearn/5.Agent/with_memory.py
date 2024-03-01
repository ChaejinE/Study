from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
query: dict = {"input": "How many letters in the word eudca"}

from langchain.agents import tool


# Define tool
@tool
def get_word_length(word: str) -> int:
    """Return the length of a word."""
    return len(word)


tools = {"get_word_length": get_word_length}

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

MEMORY_KEY = "chat_history"

# Create promopt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are very powerful assistant, but don't know current events"),
        MessagesPlaceholder(variable_name=MEMORY_KEY),
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
        MEMORY_KEY: lambda x: x.get(MEMORY_KEY),
    }
    | prompt
    | llm
    | OpenAIToolsAgentOutputParser()
)

from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=list(tools.values()), verbose=True)

from langchain_core.messages import AIMessage, HumanMessage

chat_history = []

input1 = "how many letters in the word educa?"
result = agent_executor.invoke({"input": input1, MEMORY_KEY: chat_history})
print(f"1. First result : {result}")
chat_history.extend(
    [
        HumanMessage(content=input1),
        AIMessage(content=result["output"]),
    ]
)
input2 = "is that a real word?"
result = agent_executor.invoke(
    {"input": "is that a real word?", MEMORY_KEY: chat_history}
)
print(f"2. With memory result : {result}")
