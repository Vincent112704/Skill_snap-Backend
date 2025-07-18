from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import test, resume, resume_cleaner

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["*"] during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World from main.py"}

app.include_router(test.router, prefix="/api/v1/endpoints")
app.include_router(resume.router, prefix="/api/v1/endpoints")
app.include_router(resume_cleaner.router, prefix="/api/v1/endpoints")
