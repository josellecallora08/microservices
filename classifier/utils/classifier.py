import httpx
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
MODEL = "llama3-70b-8192"
CATEGORIES = ["Billing", "Technical Support", "Sales Inquiry", "Feedback", "Complaint", "Other"]

async def classify_text(text:str) -> str:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-type": "application/json"
    }
    instructions = (
        f"You are a text classification model. Categorize the user's message into one of the following labels:\n"
        f"{', '.join(CATEGORIES)}.\n\n"
        "Respond with only the label. Do not add explanations, comments, or introductions."
    )
    payload = {
        "model": MODEL,
        "messages": [
            {"role":"system", "content":instructions},
            {"role":"user", "content": text}
        ],
        "temperature": 0.0
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url,headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Groq API Error: {response.text}")
    
    label = response.json()["choices"][0]["message"]["content"].strip()
    return {"category": label}