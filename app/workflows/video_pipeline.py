from app.services.youtube_service import download_audio
from app.services.whisper_service import transcribe_audio
from app.services.llm_service import generate_assets
from app.services.storage_service import FilestorageService
import logging

storage = FilestorageService()

def process_youtube_video(youtube_url: str) -> dict:

    """
    Full pipeline to process a Youtube video URL into generated assets.

    Args:
        youtube_url (str): The URL of the Youtube video.
    
    Returns:
        GeneratedAssets: The generated assets for the video.

    """
    audio_info: dict = download_audio(youtube_url)
    transcript : dict = transcribe_audio(audio_info["file_path"])
    assets = generate_assets(youtube_url, transcript)
    data = assets.model_dump()
    storage.save_json("generated_assets", audio_info["video_id"], data)

    return data

