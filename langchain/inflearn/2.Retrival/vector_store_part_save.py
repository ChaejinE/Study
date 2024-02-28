from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma

file_path = "fortune_500_2020.csv"
loader = CSVLoader(file_path=file_path)
data = loader.load()

text_spliter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
documents = text_spliter.split_documents(data)

embedding_model = OpenAIEmbeddings()
db = Chroma.from_documents(
    documents, embedding_model, persist_directory="./fortune_500_db"
)
db.persist()  # save
