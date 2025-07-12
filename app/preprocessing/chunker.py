from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunker (path: str) -> list:
    loader = PyMuPDFLoader(path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=70)
    contents = ""
    for doc in docs: 
        contents += doc.page_content + "\n" 
    chunk = text_splitter.split_text(contents)
    return chunk
    
chunker("app/preprocessing/sample.pdf")