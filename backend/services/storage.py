from pathlib import Path
from typing import BinaryIO
from uuid import UUID

from backend.database import get_supabase

async def store_video(file: BinaryIO, video_id: UUID) -> str:
    """Store video file in Supabase Storage."""
    # Placeholder: implement Supabase storage upload
    return f"videos/{video_id}/video.mp4"

async def get_video(video_id: UUID) -> Path:
    """Get video file from Supabase Storage."""
    # Placeholder: implement Supabase storage download
    return Path(f"/tmp/{video_id}/video.mp4")