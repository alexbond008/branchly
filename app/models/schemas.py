from pydantic import BaseModel
from typing import Optional, List

class GeneratedAssets(BaseModel):
    video_url: str
    title_suggestions: List[str]
    timestamps: List[str]
    description: str
    hashtags: List[str]
    linkedin_post: str
    twitter_post: str
