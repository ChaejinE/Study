from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_openai.embeddings import OpenAIEmbeddings

file_path = "csv_sample.csv"
loader = CSVLoader(file_path=file_path)
data = loader.load()

embedding_model = OpenAIEmbeddings()
embeddings = embedding_model.embed_documents([text.page_content for text in data])
print(f"1. embedding num : {len(embeddings)}")
query = embedding_model.embed_query("What was the name entioned in the converstaion?")
print(f" query : {query[:5]}")
