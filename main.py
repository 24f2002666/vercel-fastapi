from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

# Load the JSON data
with open('q-vercel-python.json') as f:
    students_data = json.load(f)

# Create FastAPI instance
app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# GET /api?name=X&name=Y...
@app.get("/api")
async def get_marks(
    name: List[str] = Query(
        ..., 
        description="One or more ?name=… query params, e.g. ?name=Alice&name=Bob"
    )
):
    # Build lookup dict
    student_dict = {s["name"]: s["marks"] for s in students_data}

    # Fetch marks in request order
    marks = [ student_dict.get(n) for n in name ]
    return JSONResponse(content={"marks": marks})
