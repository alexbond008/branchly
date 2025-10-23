from fastapi import FastAPI

from backend.routes.health import router as health_router
from backend.routes.upload import router as upload_router

app = FastAPI(title="branchly", version="0.1.0")

app.include_router(health_router)
app.include_router(upload_router, prefix="/upload", tags=["upload"]) 


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
