from langchain.memory import ConversationSummaryBufferMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)
# History, summary are saved all in this memory
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=10)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "not much you"}, {"output": "not much"})
result = memory.load_memory_variables(dict())
print(f"1. Summary buffer mem : {result}")
# 1. summary buffer mem : {'history': 'System: The human greets the AI with a simple "hi." The AI responds by asking "what\'s up," to which the human replies "not much, you."\nAI: not much'}

memory = ConversationSummaryBufferMemory(
    llm=llm, max_token_limit=10, return_messages=True
)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "not much you"}, {"output": "not much"})
result = memory.load_memory_variables({})
print(f"2. Summary buffer mem : {result}")
# 2. summary buffer mem : {'history': [SystemMessage(content='The human greets the AI with a simple "hi." The AI responds by asking "what\'s up," to which the human replies "not much, you."'), AIMessage(content='not much')]}

messages = memory.chat_memory.messages
prev_summary = ""
new_summary = memory.predict_new_summary(
    messages=messages, existing_summary=prev_summary
)
print(f"3. New summary : {new_summary}")
# 3. New summary : The human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good because it will help humans reach their full potential. The AI doesn't have much to say on the topic.
