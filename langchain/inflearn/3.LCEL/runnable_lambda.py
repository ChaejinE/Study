def length_function(text):
    return len(text)


def multiple_length_function(_dict):
    def _multiple_length_function(text1, text2):
        return len(text1) * len(text2)

    return _multiple_length_function(_dict["text1"], _dict["text2"])


from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableLambda
from operator import itemgetter

prompt = ChatPromptTemplate.from_template("what is {a} + {b}")
model = ChatOpenAI()

chain = (
    {
        "a": itemgetter("foo") | RunnableLambda(length_function),
        "b": {"text1": itemgetter("foo"), "text2": itemgetter("bar")}
        | RunnableLambda(multiple_length_function),
    }
    | prompt
    | model
)
query = {"foo": "bar", "bar": "gah"}
print(f"1. Chain : {chain.invoke(query)}")
