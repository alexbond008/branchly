from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, HttpUrl

class AssetType(str, Enum):
    TWEETS = "tweets"
    LINKEDIN = "linkedin"
    TITLES = "titles"
    BLOG = "blog"

class User(BaseModel):
    id: UUID
    email: str
    auth_id: str
    created_at: datetime

class Video(BaseModel):
    id: UUID
    user_id: UUID
    title: str
    url: HttpUrl
    transcript_text: Optional[str]
    created_at: datetime

class GeneratedAsset(BaseModel):
    id: UUID
    video_id: UUID
    asset_type: AssetType
    content: dict  # JSON content varies by asset_type
    created_at: datetime

# Request/Response models
class VideoUploadRequest(BaseModel):
    url: Optional[HttpUrl] = None
    # file upload handled by Form/UploadFile in route

class VideoResponse(BaseModel):
    video_id: UUID
    status: str