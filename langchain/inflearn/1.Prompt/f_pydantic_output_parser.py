from typing import List
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain_openai import ChatOpenAI

model = ChatOpenAI(temperature=0)


class Joke(BaseModel):
    # description을 넣으면 더 잘 동작한다고한다.
    ## instruction에 string으로 들어가기 때문으로 보인다.
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")

    @validator("setup")
    def question_ends_with_question_mark(cls, field):
        if field[-1] != "?":
            raise ValueError("Badly formed question !")
        return field


joke_query = "Tell me a joke"

parser = PydanticOutputParser(pydantic_object=Joke)
print("parser's instruction : ", parser.get_format_instructions())
prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser
result = chain.invoke({"query": joke_query})
print(f"result : {result}\ntype : {type(result)}")


class Actor(BaseModel):
    name: str = Field(description="name of an actor")
    file_names: List[str] = Field(description="list of names of films they starred in")


actor_query = "Generate the filmograhpy for a random actor."
parser = PydanticOutputParser(pydantic_object=Actor)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser
result = chain.invoke({"query": actor_query})
print(f"Actor Result : {result}\n type: {type(result)}")
