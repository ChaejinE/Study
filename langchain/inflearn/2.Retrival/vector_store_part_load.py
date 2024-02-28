from langchain_community.vectorstores.chroma import Chroma
from vector_store_part_save import embedding_model

db = Chroma(persist_directory="./fortune_500_db", embedding_function=embedding_model)
query = "What is JPMorgan Revenue ?"
docs = db.similarity_search(query)
print(f"1. docs : \n{docs[0].page_content}\ndocuments num : {len(docs)}")
