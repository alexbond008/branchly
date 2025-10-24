from fastapi import FastAPI
from backend.routes.health import router as health_router

app = FastAPI(
    title="Branchly",
    version="0.1.0")

app.include_router(
    health_router,
    tags=["health"]
)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
