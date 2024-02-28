from langchain_community.document_loaders.csv_loader import CSVLoader

file_path = "csv_sample.csv"
loader = CSVLoader(file_path=file_path)
data = loader.load()
print(f"1. csv load result : {data}\ntype: {type(data)}")

loader = CSVLoader(file_path=file_path, csv_args={"delimiter": ",", "quotechar": '"'})
data = loader.load()
print(f"2. csv load result : {data}\ntype: {type(data)}")

# About no field names
file_path = "csv_sample_nohead.csv"
loader = CSVLoader(
    file_path=file_path,
    csv_args={
        "delimiter": ",",
        "quotechar": '"',
        "fieldnames": ["name", "age", "counrtykkokko"],
    },
)
data = loader.load()
print(f"3. no head csv load result : {data}\ntype: {type(data)}")

file_path = "csv_sample.csv"
loader = CSVLoader(file_path=file_path, source_column="country")
data = loader.load()
print(f"4. csv load result : {data}\ntype: {type(data)}")

from langchain_community.document_loaders import UnstructuredHTMLLoader, BSHTMLLoader

file_path = "html_sample.html"
loader = UnstructuredHTMLLoader(file_path=file_path)
data = loader.load()
print(f"1. html load result : {data}")

loader = BSHTMLLoader(file_path=file_path)
data = loader.load()
print(f"2. html load result : {data}")

from langchain_community.document_loaders import PyPDFLoader

file_path = "csv_sample.pdf"
loader = PyPDFLoader(file_path=file_path)
pages = loader.load_and_split()
print(f"1. pdf load result : {pages[0]}")
