from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
async def root():
    return {"message": "Hello World from app/api/v1/endpoints/test.py"}