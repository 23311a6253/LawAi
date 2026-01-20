from fastapi import FastAPI
from pydantic import BaseModel

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
    """
    Placeholder endpoint.

    Real logic will be plugged in later:
    - intent resolution
    - concept retrieval
    - AI explanation
    """

    return QueryResponse(
        explanation="This is a placeholder response. AI integration will be added later.",
        applicable_law="N/A",
        authority="India Code – Government of India",
        disclaimer="This information is for legal awareness only and does not replace professional legal advice."
    )
