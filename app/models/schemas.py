from pydantic import BaseModel
from typing import Optional, List

class Video(BaseModel):
    url: str # we can use this as the id of the video as its unique
    title: Optional[str] = None
    description: Optional[str] = None

class GeneratedAssets(BaseModel):
    video_url: str
    title_suggestions: List[str]
    timestamps: List[str]
    summary: str
    hashtags: List[str]
    linkedin_post: str
    twitter_post: str