from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from utils.summarizer import summarize_text

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/summarize")
async def summarize(input: TextInput):
    try:
        result = await summarize_text(input.text)
        return {"summary": result}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))