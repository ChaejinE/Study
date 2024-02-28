from langchain.text_splitter import RecursiveCharacterTextSplitter

state_of_the_union: str = ""


def load_text_in_file(file_path: str) -> str:
    global state_of_the_union
    with open(file_path) as f:
        state_of_the_union = f.read()


file_path = "state_of_the_union.txt"
load_text_in_file(file_path)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)
texts = text_splitter.create_documents([state_of_the_union])
print(f"1. text spliter recursive character result : {texts[0]}, {texts[1]}")

from langchain.text_splitter import CharacterTextSplitter

# Split using token
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=100, chunk_overlap=0
)
texts = text_splitter.split_text(state_of_the_union)
print(f"2. text spliter tiktoken encoder result : {texts[0]}, {texts[1]}")
