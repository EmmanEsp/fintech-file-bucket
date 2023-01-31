from fastapi import FastAPI

from app.api import healthcheck


def init():
    """
    Initialize the app:
    - Configure FastAPI app
    - Configure the healthcheck route
    - Configure routing path for v1 endpoints
    """
    _app = FastAPI(
        title="fastapi-template",
        description="Template allow to create services with a base code",
        version="0.1.0"
    )

    _app.include_router(
        healthcheck.router,
        prefix="/healthcheck",
        tags=["Health"]
    )

    return _app


app = init()
