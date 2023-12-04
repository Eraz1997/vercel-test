from fastapi import APIRouter

from backend.routes.healthy.constants import HEALTHY_ROUTES_PREFIX
from backend.routes.healthy.models import GetHealthResponse


def create_router() -> APIRouter:
    router = APIRouter(prefix=HEALTHY_ROUTES_PREFIX)

    @router.get("")
    async def get_health() -> GetHealthResponse:
        return GetHealthResponse()

    return router
