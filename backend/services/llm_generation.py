from typing import Dict, List
from openai import AsyncOpenAI

from backend.config import settings
from backend.models import AssetType

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

async def generate_content(
    transcript: str,
    asset_types: List[AssetType]
) -> Dict[AssetType, dict]:
    """Generate content from transcript using GPT."""
    # Placeholder: implement GPT API calls
    return {
        AssetType.TWEETS: {"tweets": []},
        AssetType.LINKEDIN: {"post": ""},
        AssetType.TITLES: {"titles": []},
    }