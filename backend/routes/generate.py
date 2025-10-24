from fastapi import APIRouter
from typing import List, Optional
from uuid import UUID

from backend.models import AssetType
from backend.services.llm_generation import generate_content

router = APIRouter()

@router.post("/{video_id}")
async def generate_assets(
    video_id: UUID,
    content_types: Optional[List[AssetType]] = None
):
    """Generate assets from video transcript."""
    # Placeholder: will implement service calls
    return {"status": "processing"}