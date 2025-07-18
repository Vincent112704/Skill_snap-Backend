from fastapi import APIRouter, UploadFile, File
from app.preprocessing.extractor import PDF_extractor
router = APIRouter()

@router.post("/resume")
async def extract_resume_data(File: UploadFile = File(...)):
    contents = await PDF_extractor(File)

    return {
        "message": "Resume data extracted successfully",
        "contents": contents, 
        "status": 200
    }
