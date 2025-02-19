from fastapi import FastAPI
from pydantic import BaseModel
from agent.agent import run_agent

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask_agent(request: QueryRequest):
    response = run_agent(request.query)
    return {"response": response}
