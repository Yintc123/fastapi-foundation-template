from fastapi import APIRouter, Depends
from app.core.config import BaseAppSettings, get_app_settings

router: APIRouter = APIRouter()

@router.get("/health")
def health(settings: BaseAppSettings = Depends(get_app_settings)):
    return {
        "message": "ok",
        "app_version": settings.app_version
    }
