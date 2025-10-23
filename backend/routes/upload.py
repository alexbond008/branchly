from fastapi import APIRouter

router = APIRouter()

@router.post("/video")
async def upload_video(url: str = None):
    # Minimal placeholder: accept YouTube URL or uploaded file in future
    if not url:
        return {"error": "no url provided"}
    return {"video_id": "fake-video-id", "status": "queued"}
