import httpx
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # store this in .env or compose later

async def transcribe_audio(file_path: str) -> str:
    url = "https://api.groq.com/openai/v1/audio/transcriptions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    files = {
        "file": open(file_path, "rb"),
        "model": (None, "whisper-large-v3-turbo"),
        "language": (None, "en")
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, files=files)

    if response.status_code != 200:
        raise Exception(f"Groq API error: {response.text}")

    return response.json()["text"]

