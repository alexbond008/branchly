from fastapi import APIRouter
from uuid import UUID

from backend.services.transcription import transcribe_video

router = APIRouter()

@router.post("/{video_id}")
async def transcribe(video_id: UUID):
    """Transcribe a video using Whisper API."""
    # Placeholder: will implement service call
    return {"status": "processing"}