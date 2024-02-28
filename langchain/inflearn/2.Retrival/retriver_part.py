from vector_store_part_load import db

# Use Retreiver
retriever = db.as_retriever()
result = retriever.get_relevant_documents("walmart")
print(f"1. result as retriever :\n{result[0].page_content}")

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings

loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
splits = text_splitter.split_documents(data)

embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents=splits, embedding=embedding)

from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI

question = "What are the approaches to Task Decomposition ?"
llm = ChatOpenAI(temperature=0)
retriever_from_llm = MultiQueryRetriever.from_llm(
    retriever=vectordb.as_retriever(), llm=llm
)

import logging

logging.basicConfig(level=logging.INFO)

unique_docs = retriever_from_llm.get_relevant_documents(query=question)
print(f"1. result len : {len(unique_docs)}\n{unique_docs[0] if unique_docs else ''}")
