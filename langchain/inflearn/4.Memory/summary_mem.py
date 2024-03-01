from langchain.memory.summary import ConversationSummaryMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)
memory = ConversationSummaryMemory(llm=llm)
memory.save_context({"input": "hi"}, {"output": "whats up"})
result = memory.load_memory_variables(dict())
print(f"1. Summary : {result}")
# 1. Summary : {'history': 'The human greets the AI with a simple "hi" and the AI responds by asking "what\'s up."'}
memory.return_messages = True
result = memory.load_memory_variables(dict())
print(f"2. Summary when return messages is True : {result}")
# 2. Summary when return messages is True : {'history': [SystemMessage(content='The human greets the AI with a simple "hi" and the AI responds by asking "what\'s up."')]}

memory.save_context({"input": "bye"}, {"output": "good bye"})
messages = memory.chat_memory.messages
print(f"3. messages : {messages}")
# 3. messages : [HumanMessage(content='hi'), AIMessage(content='whats up'), HumanMessage(content='bye'), AIMessage(content='good bye')]

prev_summary = result
result = memory.predict_new_summary(messages=messages, existing_summary=prev_summary)
print(f"4. Predict new summary : {result}, {type(result)}")
# 4. Predict new summary : The human greets the AI with a simple "hi" and the AI responds by asking "what's up." The human then says "bye" and the AI responds with "good bye.", <class 'str'>
from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()
history.add_user_message("hi")
history.add_ai_message("hi there!")
print(f"5. ChatMessageHistory Object Test -> {history}\n{type(history)}")
"""
5. ChatMessageHistory Object Test -> Human: hi
AI: hi there!
"""

history = ChatMessageHistory(messages=messages)
memory = ConversationSummaryMemory.from_messages(
    llm=llm, chat_memory=history, return_messages=True
)
buffer = memory.buffer
print(f"6. {messages}\n-> Buffer : {memory.buffer}")
"""
6. [HumanMessage(content='hi'), AIMessage(content='whats up'), HumanMessage(content='bye'), AIMessage(content='good bye')]
-> Buffer : The human greets the AI with a simple "hi" and the AI responds by asking "what's up." The human then says "bye" and the AI responds with "good bye."
"""

memory = ConversationSummaryMemory.from_messages(
    llm=llm, buffer=buffer, chat_memory=history, return_messages=True
)
print(f"7. {messages}\n-> Buffer with buffer argument : {memory.buffer}")
"""
7. [HumanMessage(content='hi'), AIMessage(content='whats up'), HumanMessage(content='bye'), AIMessage(content='good bye')]
-> Buffer with buffer argument : The human greets the AI with a simple "hi" and the AI responds by asking "what's up." The human then says "bye" and the AI responds with "good bye."
"""
