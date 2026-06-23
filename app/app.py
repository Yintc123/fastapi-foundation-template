from fastapi import FastAPI
from .api import api_router

def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        title = "fastapi-foundation-template",
        version = "1.0.0"
    )

    app.include_router(api_router)

    return app