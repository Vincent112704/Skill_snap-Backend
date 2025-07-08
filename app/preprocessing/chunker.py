from langchain_community.document_loaders import PyMuPDFLoader

path = "test_data/Vincent_Bacalso_CV2.pdf"
loader = PyMuPDFLoader(path)
docs = loader.load()
print(docs[0].page_content)