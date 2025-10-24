from fastapi import APIRouter
from uuid import UUID

from backend.database import get_supabase

router = APIRouter()

@router.get("/{video_id}")
async def get_assets(video_id: UUID):
    """Get all generated assets for a video."""
    # Placeholder: will implement database query
    return {"assets": []}