from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.api import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 App TaskHub đang được khởi tạo...")
    yield
    print("🛑 App TaskHub đang đóng kết nối...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/", tags=["Health Check"])
def root():
    return {"message": "Chào mừng đến với TaskHub API!", "docs": "/docs"}
