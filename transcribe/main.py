from fastapi import FastAPI, UploadFile, File, HTTPException
from utils.groq_client import transcribe_audio
import tempfile

app = FastAPI()

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    if not file.filename.endswith((".mp3", ".wav", ".m4a")):
        raise HTTPException(status_code=400, detail="Unsupported file type")

    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=file.filename) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        result = await transcribe_audio(tmp_path)
        return {"transcription": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

