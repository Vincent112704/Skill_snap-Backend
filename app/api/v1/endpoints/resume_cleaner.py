from fastapi import APIRouter, UploadFile, File
from app.preprocessing.extractor import text_cleaner, text_to_line, text_to_structured_sections

router = APIRouter()

@router.post("/upload")
def resume_cleaner(body: str):
    res = text_to_structured_sections(text_to_line(text_cleaner(text)))

    return {
        "message": "File cleaned", 
        "content": res, 
        "status": 200
    }