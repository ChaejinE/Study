from operator import itemgetter
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

# Example 1
prompt1 = ChatPromptTemplate.from_template("what is the city {person} is from?")
prompt2 = ChatPromptTemplate.from_template(
    "what country is the city {city} in? respond in {language}"
)

model = ChatOpenAI()
parser = StrOutputParser()

chain1 = prompt1 | model | parser
chain2 = {"city": chain1, "language": itemgetter("language")} | prompt2 | model | parser
chain2_result = chain2.invoke({"person": "obama", "language": "south korean"})
print(f"1. chain2_result : {chain2_result}")

from langchain_core.runnables import RunnablePassthrough

runnable_passtorugh = RunnablePassthrough()

# Example 2
prompt1 = ChatPromptTemplate.from_template(
    "generate a {attribute} color. Return the name of the color and nothing else:"
)
prompt2 = ChatPromptTemplate.from_template(
    "what is a fruit of color: {color}. Return the name of the fruit and nothing else:"
)
prompt3 = ChatPromptTemplate.from_template(
    "what is a country with a flag that has the color: {color}. Return the name of the country and nothing else:"
)
prompt4 = ChatPromptTemplate.from_template(
    "What is the color of {fruit} and the flag of {country}?"
)

model_parser = model | parser

color_generator = {"attribute": runnable_passtorugh} | prompt1 | {"color": model_parser}
color_to_fruit = prompt2 | model_parser
color_to_country = prompt3 | model_parser
question_generator = (
    color_generator | {"fruit": color_to_fruit, "country": color_to_country} | prompt4
)
prompt = question_generator.invoke("warm")
print(f"2-1. question generator result : {prompt}, {type(prompt)}")
result = model.invoke(prompt)
print(f"2-2. result : {result}, {type(result)}")

# Example 3
"""
     Input
      / \
     /   \
 Branch1 Branch2
     \   /
      \ /
      Combine
"""
planner = (
    ChatPromptTemplate.from_template("Generate an argument about: {input}")
    | model
    | parser
    | {"base_response": runnable_passtorugh}
)

## branch 1
arguments_for = (
    ChatPromptTemplate.from_template(
        "List the pros or positive aspects of {base_response}"
    )
    | model
    | parser
)

## branch 2
arguments_against = (
    ChatPromptTemplate.from_template(
        "List the cons or negative aspects of {base_response}"
    )
    | model
    | parser
)

final_responder = (
    ChatPromptTemplate.from_messages(
        [
            ("ai", "{original_response}"),
            ("human", "Pros:\n{results_1}\n\nCons:\n{results_2}"),
            ("system", "Generate a final response given the critique"),
        ]
    )
    | model
    | parser
)

chain = (
    planner
    | {
        "results_1": arguments_for,
        "results_2": arguments_against,
        "original_response": itemgetter("base_response"),
    }
    | final_responder
)
result = chain.invoke({"input": "scrum"})
print(f"3. Branch chain result : {result}")
