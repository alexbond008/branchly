from fastapi import APIRouter, HTTPException
from app.workflows.video_pipeline import process_youtube_video

router = APIRouter()

@router.post("/process_youtube_video")
async def process_video_endpoint(youtube_url: str):
    """
    Endpoint to process a Youtube video URL into generated assets.

    Args:
        youtube_url (str): The URL of the Youtube video.
    
    Returns:
        dict: The generated assets for the video.

    """
    try:
        assets = process_youtube_video(youtube_url)
        return {"status": "success", "data": assets}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))