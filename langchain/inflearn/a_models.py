from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

import os

os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI()
chat_model = ChatOpenAI()

from langchain.schema import SystemMessage, HumanMessage

text = "What would be a good company name for a company taht makes colorful socks?"
messages = [SystemMessage(content="You are the teenager"), HumanMessage(content=text)]

result = llm.invoke(text)
print(f"LLM : {result} type : {type(result)}")
result = chat_model.invoke(messages)
print(f"Chat Models : {result} type : {type(result)}")
