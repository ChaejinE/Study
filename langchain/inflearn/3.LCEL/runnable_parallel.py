from langchain.schema.runnable import RunnableParallel, RunnablePassthrough

runnable = RunnableParallel(passed=RunnablePassthrough())
query = {"num": 1}
print(f"1. RunanableParallel : {runnable.invoke(query)}")
# 1. RunanableParallel : {'passed': {'num': 1}}

runnable = RunnableParallel(
    passed=RunnablePassthrough(),
    extra=RunnablePassthrough.assign(mult=lambda x: x["num"] * 3),
    modified=lambda x: x["num"] + 1,
)
print(f"2. RunanableParallel : {runnable.invoke(query)}")
# 2. RunanableParallel : {'passed': {'num': 1}, 'extra': {'num': 1, 'mult': 3}, 'modified': 2}

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

model = ChatOpenAI()

joke_chain = ChatPromptTemplate.from_template("tell me a joke about {topic}") | model
poem_chain = (
    ChatPromptTemplate.from_template("write a 2-line opem about {topic}") | model
)

map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)
query = {"topic": "bear"}
print(f"3. map_chain : {map_chain.invoke(query)}")
# 3. map_chain : {'joke': AIMessage(content='What do you call a bear with no teeth?\n\nA gummy bear!'), 'poem': AIMessage(content='In the stillness of the forest, the bear roams free,\nA majestic creature of strength and mystery.')}
