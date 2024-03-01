from langchain.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase

template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
SQL Query:"""
prompt = ChatPromptTemplate.from_template(template)

db = SQLDatabase.from_uri("sqlite:///./Chinook.db")

from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough


get_db_schema = lambda _: db.get_table_info()


model = ChatOpenAI()
sql_response = (
    RunnablePassthrough.assign(schema=get_db_schema)
    | prompt
    | model.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)
result = sql_response.invoke({"question": "How many employees are there?"})
print(f"1. sql chain : {result}")

template = """Based on the table schema below, question, sql query, and sql response, write a natural language response:
{schema}

Question: {question}
SQL Query: {query}
SQL Response: {response}"""
prompt_response = ChatPromptTemplate.from_template(template)

full_chain = (
    RunnablePassthrough.assign(query=sql_response)
    | RunnablePassthrough.assign(
        schema=get_db_schema, response=lambda x: db.run(x.get("query"))
    )
    | prompt_response
    | model
)
result = full_chain.invoke({"question": "How many employees are there?"})
print(f"2. Full cahin : {result}")
