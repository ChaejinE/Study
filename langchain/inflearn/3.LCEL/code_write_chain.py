from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain_community.utilities.python import PythonREPL

# Introduce PythonREPL
python_repl = PythonREPL()
result = python_repl.run("print(1+1)")
print(f"1. print(1+1) : {result}")

template = """Write some python code to solve the user's problem. 

Return only python code in Markdown format, e.g.:

```python
....
```"""
prompt = ChatPromptTemplate.from_messages([("system", template), ("human", "{input}")])
model = ChatOpenAI()


def _sanitize_output(text: str):
    _, after = text.split("```python")
    return after.split("```")[0]


chain = prompt | model | StrOutputParser()
query = {
    "input": "Write the function to sort the list. Then call the function by pasing [1,4,2]"
}
result = chain.invoke(query)
print(f"2. chain : {result}")
repl_chain = chain | _sanitize_output | PythonREPL().run
print(f"3. repl chain : {repl_chain.invoke(query)}")
