from fastapi import FastAPI
from pydantic import BaseModel
import json
from pathlib import Path

DATA_FILE = Path("data/labour_law.json")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    labour_data = json.load(f)

app = FastAPI(
    title="LawAI",
    description="AI-powered legal awareness system",
    version="1.0.0"
)


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    explanation: str
    applicable_law: str
    authority: str
    disclaimer: str


@app.get("/")
def health_check():
    return {"status": "LawAI is running"}

@app.post("/query", response_model=QueryResponse)
def handle_query(request: QueryRequest):
    user_query = request.query.lower()

    # Temporary simple intent detection
    if "child" in user_query or "kids" in user_query:
        concept = labour_data["concepts"][0]

        return QueryResponse(
            explanation=concept["concept_description"]["en"],
            applicable_law=concept["applicable_acts"][0]["act_name"],
            authority=concept["applicable_acts"][0]["authority"],
            disclaimer="This information is for legal awareness only and does not replace professional legal advice."
        )

    return QueryResponse(
        explanation="No verified legal information found for this query.",
        applicable_law="N/A",
        authority="India Code – Government of India",
        disclaimer="This information is for legal awareness only and does not replace professional legal advice."
    )
