from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="SmartCut Luxury API",
    description="API for SmartCut Luxury business management",
    version="1.0.0"
)

# MongoDB connection
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "smartcut_luxury")

try:
    client = MongoClient(MONGODB_URI)
    db = client[DATABASE_NAME]
    print("✅ Connected to MongoDB")
except Exception as e:
    print(f"❌ MongoDB connection error: {e}")

# CORS configuration
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "[\"http://localhost:3000\"]").replace("'", '"')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to SmartCut Luxury API",
        "status": "running",
        "database": DATABASE_NAME
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "SmartCut Luxury API"}

# Sample endpoint
@app.get("/api/info")
def get_info():
    return {
        "name": "SmartCut Luxury",
        "type": "Business Management System",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    PORT = int(os.getenv("API_PORT", 8000))
    HOST = os.getenv("API_HOST", "0.0.0.0")
    uvicorn.run(app, host=HOST, port=PORT)
