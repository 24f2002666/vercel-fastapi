from fastapi import FastAPI
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
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET"],  # Allow only GET methods
    allow_headers=["*"],
)

# Create an endpoint to get student marks
@app.get("/api")
async def get_marks(name: List[str]):  # Expecting a list of 'name' query parameters
    marks = []
    
    # Create a dictionary for quick lookup
    student_dict = {student["name"]: student["marks"] for student in students_data}
    
    for student_name in name:
        # Fetch marks for each student
        mark = student_dict.get(student_name)
        if mark is not None:
            marks.append(mark)
        else:
            marks.append(None)  # If the student name is not found, append None

    return JSONResponse(content={"marks": marks})
