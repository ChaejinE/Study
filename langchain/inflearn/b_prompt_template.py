from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "What would be a good company name for a company taht makes {product}?"
)
prompt_output = prompt.format(product="noodle")
print(f"prompt output : {prompt_output}")

from langchain.prompts.chat import ChatPromptTemplate

template = (
    "You are a helpful assistant that translates {input_language} to {output_language}."
)
human_template = "{text}"

# system : role
# human : content
chat_prompt = ChatPromptTemplate.from_messages(
    [("system", template), ("human", human_template)]
)
chat_prompt_output = chat_prompt.format_messages(
    input_language="English", output_language="French", text="I love noodle"
)
print(f"chat prompt output : {chat_prompt_output}")
