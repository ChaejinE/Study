from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
result = prompt.invoke({"topic": "ice cream"})
print(f"1. prompt : {result}")
# 1. prompt : messages=[HumanMessage(content='tell me a short joke about ice cream')]

from langchain_openai import ChatOpenAI

model = ChatOpenAI()
result = model.invoke(result)
print(f"2. model : {result}")
# 2. model : content='Why did the ice cream break up with the cone? It was too cold and cone-flicting!'

from langchain.schema.output_parser import StrOutputParser

parser = StrOutputParser()
result = parser.parse(result)
print(f"3. output parser : {result}")
# 3. output parser : content='Why did the ice cream go to therapy? Because it had too many sprinkles of anxiety!'

chain = prompt | model | parser
result = chain.invoke({"topic": "ice cream"})
print(f"4. chain : {result}")
