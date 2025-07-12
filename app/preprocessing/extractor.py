from langchain_community.document_loaders import PyMuPDFLoader


def PDF_extractor (path: str) -> str:
    loader = PyMuPDFLoader(path)
    docs = loader.load()
    contents = ""
    for doc in docs: 
        contents += doc.page_content 
    return contents

def text_cleaner(raw_text: str)-> str:
    bullet_chars = ['\u2022', '\u2013', '\u2014', '\u25AA', '\u25E6', '-', '*']
    cleaned_text = raw_text

    for bullet in bullet_chars:
        cleaned_text = cleaned_text.replace(bullet, '-')

    cleaned_text = cleaned_text.replace("\n", " ")
    cleaned_text = cleaned_text.replace("\r", " ")
    cleaned_text = cleaned_text.replace("\t", " ")
    cleaned_text = cleaned_text.replace('\xa0', ' ')
    cleaned_text = cleaned_text.replace('\u200b', ' ')
    cleaned_text = cleaned_text.replace('\u2028', ' ')
    cleaned_text = cleaned_text.replace('\u2029', ' ')
    cleaned_text = cleaned_text.replace('\ufeff', '')
    cleaned_text = cleaned_text.replace('|', ' ')
    cleaned_text = cleaned_text.lower()

    return cleaned_text.strip()



# PDF_extractor("test_data/Vincent_Bacalso_CV2.pdf")
text_cleaner(PDF_extractor("test_data/Vincent_Bacalso_CV2.pdf"))

    
