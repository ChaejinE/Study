from langchain.output_parsers.enum import EnumOutputParser
from enum import Enum


class Colors(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


parser = EnumOutputParser(enum=Colors)
print(parser.parse("red "))
print(parser.parse("\nred "))

try:
    parser.parse("yellow")
except Exception as e:
    print(e)
