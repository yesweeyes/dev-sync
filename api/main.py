from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/foo")
async def submit_form(data: dict):
    print(data)
    if data is not None:
        return {"message": "Form submitted successfully"}
    raise HTTPException(status_code=400, detail="Failed to submit form")
