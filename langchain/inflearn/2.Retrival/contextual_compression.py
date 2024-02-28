from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

file_path = "state_of_the_union.txt"
data = TextLoader(file_path=file_path).load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
splits = text_splitter.split_documents(data)

embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents=splits, embedding=embedding)

retriever = vectordb.as_retriever()
query = "What did the president say about Ketanji Brown Jackson"
docs = retriever.get_relevant_documents(query)
print(f"Normal  result no comporession:\n{docs}")

llm = OpenAI(temperature=0)
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=retriever
)
compressed_docs = compression_retriever.get_relevant_documents(query)
print(f"compressor result :\n{compressed_docs}")
