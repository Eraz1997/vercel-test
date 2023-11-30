from fastapi import APIRouter
from fastapi.responses import JSONResponse
from routes.public.v1.test.constants import PUBLIC_V1_TEST_API_PREFIX


def create_router() -> APIRouter:
    router = APIRouter(prefix=PUBLIC_V1_TEST_API_PREFIX)

    @router.get("")
    async def test() -> JSONResponse:
        """Test endpoint."""

        return JSONResponse({"message": "okay!"})

    return router
