from pathlib import Path
from openai import AsyncOpenAI

from backend.config import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

async def transcribe_audio(audio_path: Path) -> str:
    """Transcribe audio file using Whisper API."""
    # Placeholder: implement Whisper API call
    return "Transcript text will go here"