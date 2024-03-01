from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser

chain = (
    PromptTemplate.from_template(
        """Given the user question below, classify it as either being about `Strawberry`, `Banana`, or `Other`.

Do not respond with more than one word.

<question>
{question}
</question>

Classification:"""
    )
    | ChatOpenAI()
    | StrOutputParser()
)
query = {"question": "What is the fruit that has red color ?"}
print(f"1. chain : {chain.invoke(query)}")

strawberry_chain = (
    PromptTemplate.from_template(
        """You are an expert about strawberry. \
Always answer questions starting with "As a Strawberry expert ... ". \
Respond to the following question:

# Question: {question}
# Answer:"""
    )
    | ChatOpenAI()
)

banana_chain = (
    PromptTemplate.from_template(
        """You are an expert about banana. \
Always answer questions starting with "As a Banana expert ... ". \
Respond to the following question:

# Question: {question}
# Answer:"""
    )
    | ChatOpenAI()
)

general_chain = (
    PromptTemplate.from_template(
        """Respond to the following question:

Question: {question}
Answer:"""
    )
    | ChatOpenAI()
)

from langchain.schema.runnable import RunnableBranch

branch = RunnableBranch(
    (lambda x: "strawberry" in x["topic"].lower(), strawberry_chain),
    (lambda x: "banana" in x["topic"].lower(), banana_chain),
    general_chain,
)

full_chain = {"topic": chain, "question": lambda x: x["question"]} | branch
print(
    "1. expert : ",
    full_chain.invoke({"question": "What is the fruit that has red color?"}),
)
print(
    "2. expert : ",
    full_chain.invoke({"question": "What is the fruit that has yellow color?"}),
)
print(
    "3. expert : ",
    full_chain.invoke({"question": "What is the fruit that has green color?"}),
)
