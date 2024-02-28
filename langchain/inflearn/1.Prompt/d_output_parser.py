# from typing import List
# from langchain.schema import BaseOutputParser


# class CommaSeparatedListOutputParser(BaseOutputParser[List[str]]):
#     def parse(self, text: str) -> List[str]:
#         return text.strip().split(", ")


# print(CommaSeparatedListOutputParser().parse("hi, bye"))

from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate

output_parser = CommaSeparatedListOutputParser()

format_instructions = output_parser.get_format_instructions()
print(f"instruction : {format_instructions}")
# instruction : Your response should be a list of comma separated values, eg: `foo, bar, baz`

prompt = PromptTemplate(
    template="List five {subject}.\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": format_instructions},
)

from langchain_openai import OpenAI

llm = OpenAI(temperature=0)

_input = prompt.format(subject="ice create flavors")
output = llm.invoke(_input)

print(output_parser.parse(output))
# Problem: ['1. Vanilla\n2. Chocolate\n3. Strawberry\n4. Mint chocolate chip\n5. Cookies and cream']
