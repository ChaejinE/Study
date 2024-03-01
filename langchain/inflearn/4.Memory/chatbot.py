from operator import itemgetter
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain_core.messages.ai import AIMessage

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful chatbot"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)
memory = ConversationBufferMemory(return_messages=True)
memory.chat_memory.add_user_message("hi")
memory.chat_memory.add_ai_message("What's up?")
print(f"What is the memory ? : {memory.load_memory_variables(dict())}")
# What is the memory ? : {'history': [HumanMessage(content='hi'), AIMessage(content="What's up?")]}

chain = (
    RunnablePassthrough.assign(
        history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
    )
    | prompt
    | model
)

inputs = {"input": "Hello, My name is Joon"}
response: AIMessage = chain.invoke(inputs)
print(f"1. memory chain : {response}")
# 1. memory chain : content='Hello Joon! How can I assist you today?'
memory.save_context(inputs=inputs, outputs={"ouptut": response.content})
print(f"2. Save Check : {memory.load_memory_variables(dict())}")
# 2. Save Check : {'history': [HumanMessage(content='hi'), AIMessage(content="What's up?"), HumanMessage(content='Hello, My name is Joon'), AIMessage(content='Nice to meet you, Joon! How can I assist you today?')]}

inputs["input"] = "What is my name ?"
response = chain.invoke(inputs)
print(f"3. {inputs.get('input')} : {response}")
# 3. What is my name ? : content='Your name is Joon.'
