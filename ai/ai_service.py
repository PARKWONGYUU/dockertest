from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    # 원래는 OpenAI 호출 → llm.invoke(req.message)
    # 임시로는 그냥 고정된 응답 반환
    return {
        "reply": f"🤖 (mock) 당신이 보낸 메시지: {req.message}"
    }