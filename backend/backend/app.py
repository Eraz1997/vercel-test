from fastapi import FastAPI
from backend.routes.public.v1.test.api import create_router as create_public_v1_test_api_router


def create_api_app() -> FastAPI:
    app = FastAPI()

    app.include_router(create_public_v1_test_api_router())

    return app
