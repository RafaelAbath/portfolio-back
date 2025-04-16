import os
from pydantic import BaseModel
from fastapi import FastAPI, Request
from app.rag import generate_answer, retrieve_documents

app = FastAPI()


class QueryRequest(BaseModel):

    question: str
@app.post("/query")
async def query_endpoint(payload: QueryRequest):
    if not payload.question.strip():
        return {"error": "Nenhuma pergunta foi informada."}

    answer = generate_answer(payload.question)
    return {"response": answer}
    data = await request.json()
    question = data.get("question", "")
    if not question:
        return {"error": "Nenhuma pergunta foi informada."}

    answer = generate_answer(question)
    return {"response": answer}
@app.get("/test")
async def test_supabase():
    documents = retrieve_documents("teste")
    return {"documents": documents}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)