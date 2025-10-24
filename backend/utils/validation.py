from typing import Optional
from fastapi import HTTPException
from pydantic import HttpUrl

def validate_video_url(url: Optional[HttpUrl]) -> bool:
    """Validate that URL is from supported video platform."""
    if not url:
        return False
    return any(
        platform in str(url).lower()
        for platform in ["youtube.com", "youtu.be"]
    )