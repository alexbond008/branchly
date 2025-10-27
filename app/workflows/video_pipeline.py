from app.services.youtube_service import download_audio
from app.services.whisper_service import transcribe_audio
from app.services.llm_service import generate_assets
from app.services.storage_service import FilestorageService

from app.core.logging import setup_logging
from app.core.exceptions import (
    BranchlyException,
    VideoDownloadError,
    TranscriptionError,
    AssetGenerationError,
)

import logging
from typing import Any


setup_logging()
logger = logging.getLogger(__name__)

storage = FilestorageService()


def _model_to_dict(model: Any) -> dict:
    """Convert a Pydantic model to a dict supporting v1 (.dict()) and v2 (.model_dump())."""
    if hasattr(model, "dict") and callable(getattr(model, "dict")):
        return model.dict()
    if hasattr(model, "model_dump") and callable(getattr(model, "model_dump")):
        return model.model_dump()
    if isinstance(model, dict):
        return model
    raise TypeError("Unsupported model type: cannot convert to dict")


def process_youtube_video(youtube_url: str) -> dict:

    """Full pipeline to process a Youtube video URL into generated assets.

    Args:
        youtube_url (str): The URL of the Youtube video.

    Returns:
        dict: The generated assets for the video.

    """
    logger.info("Starting processing for YouTube URL: %s", youtube_url)

    try:
        audio_info: dict = download_audio(youtube_url)
        logger.info("Downloaded audio: %s", audio_info.get("file_path"))

        transcribe_result = transcribe_audio(audio_info)
        transcript: str = transcribe_result.get("transcript")
        logger.info("Transcription complete (len=%d chars)", len(transcript or ""))

        assets = generate_assets(youtube_url, transcript)

        data = _model_to_dict(assets)
        storage.save_json("generated_assets", audio_info["video_id"], data)

        logger.info(
            "Completed processing for %s (video_id=%s)", youtube_url, audio_info.get("video_id")
        )

        return data

    except (VideoDownloadError, TranscriptionError, AssetGenerationError) as e:
        logger.exception("Processing failed for %s due to a known error: %s", youtube_url, e)
        raise
    except BranchlyException as e:
        logger.exception("Processing failed for %s with BranchlyException: %s", youtube_url, e)
        raise
    except Exception as e:
        logger.exception("Unexpected error while processing %s: %s", youtube_url, e)
        raise

