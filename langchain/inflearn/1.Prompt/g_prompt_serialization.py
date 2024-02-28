from langchain.prompts import load_prompt, PromptTemplate

template = "Tell me a {adjective} joke about {content}."
prompt = PromptTemplate(template=template, input_variables=["adjective", "content"])

file_path = "simple_prompt.yaml"
prompt.save(file_path)
prompt = load_prompt(file_path)
print(prompt.format(adjective="funny", content="chickens"))

file_path = "simple_prompt.json"
prompt.save(file_path)
prompt = load_prompt(file_path)
print(prompt.format(adjective="funny", content="chickens"))
