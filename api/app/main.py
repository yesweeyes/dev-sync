from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import router
import os

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

UPLOAD_FOLDER = "uploads"
REVIEW_FOLDER = "reviews"
OUTPUT_FOLDER = "outputs"
output_dir = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REVIEW_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/reviews", StaticFiles(directory="reviews"), name="reviews")
app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")
app.mount("/output",StaticFiles(directory="output"),name="output")

@app.get("/")
async def root():
    return {"message": "Hello World"}
