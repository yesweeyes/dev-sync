import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes import router
from app.dependencies import REQUIREMENT_DOCS_FOLDER, CODE_REVIEW_FOLDER, HLD_FOLDER, LLD_FOLDER

app = FastAPI()

# Add middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router.router)

os.makedirs(REQUIREMENT_DOCS_FOLDER, exist_ok=True)
os.makedirs(CODE_REVIEW_FOLDER, exist_ok=True)
os.makedirs(HLD_FOLDER, exist_ok=True)
os.makedirs(LLD_FOLDER, exist_ok=True)

app.mount("/app/uploads", StaticFiles(directory=REQUIREMENT_DOCS_FOLDER), name="uploads")
app.mount("/app/reviews", StaticFiles(directory=CODE_REVIEW_FOLDER), name="reviews")
app.mount("/app/output", StaticFiles(directory=HLD_FOLDER), name="output")
app.mount("/app/output", StaticFiles(directory=LLD_FOLDER), name="output")


@app.get("/")
async def root():
    return {"message": "Hello World"}
