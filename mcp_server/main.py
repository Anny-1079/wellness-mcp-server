import os
from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load wellness tips
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "wellness_tips.json")

with open(file_path, "r") as f:
    tips = json.load(f)

@app.get("/")
def root():
    return {"message": "Wellness MCP Server is running."}

@app.get("/tips/{mood}")
def get_tips(mood: str):
    mood = mood.lower()
    if mood in tips:
        return {"mood": mood, "tips": tips[mood]}
    else:
        return {"mood": mood, "tips": ["No tips available for this mood. Try another mood like happy, sad, stressed, angry, anxious."]}
