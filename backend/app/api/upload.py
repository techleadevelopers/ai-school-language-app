
# app/api/upload.py
from fastapi import APIRouter, File, UploadFile
from app.services.whisper_service import evaluate_speech_with_whisper

router = APIRouter()

@router.post("/audio/submit")
def submit_audio(file: UploadFile = File(...)):
    audio_path = f"/tmp/{file.filename}"
    with open(audio_path, "wb") as f:
        f.write(file.file.read())
    result = evaluate_speech_with_whisper(audio_path)
    return result
