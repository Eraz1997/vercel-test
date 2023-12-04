from fastapi import FastAPI
from backend.routes.healthy.router import create_router as create_health_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(create_health_router())
    return app

