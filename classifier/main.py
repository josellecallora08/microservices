from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils.classifier import classify_text

app = FastAPI()

class TextInput(BaseModel):
    text:str

@app.post("/classify")
async def classify(input: TextInput):
    try:
        result = await classify_text(input.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))