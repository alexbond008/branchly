from fastapi import FastAPI
from app.routes.video_routes import router as video_router

app = FastAPI(title="Branchly - An MVP for automated Youtube Video Content Repurposing")
app.include_router(video_router, tags=["youtube video"])