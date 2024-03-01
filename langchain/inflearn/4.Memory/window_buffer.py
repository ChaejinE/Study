from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=1)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "not much you"}, {"output": "not much"})
result = memory.load_memory_variables(dict())
print(f"1. Window memory : {result}")

# memory = ConversationBufferWindowMemory(
#     k=1, return_messages=True
# )
memory.return_messages = True
result = memory.load_memory_variables(dict())
print(f"2. Window memory when return messages is True : {result}")
