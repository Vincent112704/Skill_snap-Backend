# from langchain_community.document_loaders import PyMuPDFLoader
import fitz
from fastapi import UploadFile, File
SECTION_KEYWORDS = {
    "education": ["education", "degree", "university", "college", "school", "bachelors", "masters", "phd", "diploma"],
    "experience": ["experience", "work", "employment", "job", "position", "role", "career", "professional", "internship", "intern"],  
    "skills": ["skills", "abilities", "competencies", "expertise"],
    "certifications": ["certification", "certified", "license", "accreditation"],
}

async def PDF_extractor (file: UploadFile = File(...)) -> str:
    contents = await file.read()
    doc = fitz.open(stream=contents, filetype="pdf")

    contents = ""
    for page in doc: 
        contents += page.get_text()
    return contents

def text_cleaner(raw_text: str)-> str:
    bullet_chars = ['\u2022', '\u2013', '\u2014', '\u25AA', '\u25E6', '-', '*']
    cleaned_text = raw_text

    for bullet in bullet_chars:
        cleaned_text = cleaned_text.replace(bullet, '-')

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

def text_to_line(text: str) -> list:
    return text.split('\n')

def text_to_structured_sections(text_list: list, sections: list) -> dict:
    structured_data = {"education": [], "experience": [], "skills": [], "certifications": [], "General": []}
    for line in text_list:
        for keyword in SECTION_KEYWORDS:
            if any(word in line for word in SECTION_KEYWORDS[keyword]):
                structured_data[keyword].append(line)
            else:
                structured_data["General"].append(line)
            break
    return structured_data
    
def section_extractor(structured_data: dict) -> dict:
    '''
    Goal of this function is to extract meaningful information per structured sections
    1. parse each value of key to dig deeper into each section to extract relevant, structured information 
    2. return a dictionary with structured information per section

    Example output:
    {
        "education": {"degree": "Bachelor of Science in Computer Science", 
                      "institution": "Silliman University", 
                      "year": "2021-2023"},
        "experience": {"job_title": "Data Scientist", 
                       "company": "Tech Company", 
                       "duration": "2 years"},
        ...
    }
    
    '''
    education_info = {"degree": "", "institution": "", "year": ""}
    experience_info = {"job_title": "", "company": "", "duration": ""}
    skills_info = {"skills": []}
    certifications_info = {"certifications": []}
    general_info = {"name": "", "contact": "", "summary": ""}


# Example usage:
# text = PDF_extractor("test_data/Vincent_Bacalso_CV2.pdf")
# text_cleaned = text_cleaner(text)
# text_lines = text_to_line(text_cleaned)
# structured_output = text_to_structured_sections(text_lines, SECTION_KEYWORDS)
# print(structured_output)

    
