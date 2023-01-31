"""
Healthcheck
"""
from fastapi import APIRouter, status

from app.schemas.get_healthcheck_response import GetHealthcheckResponse

router = APIRouter()


@router.get(
    "",
    response_model=GetHealthcheckResponse,
    status_code=status.HTTP_200_OK,
)
def get_healthcheck():
    """
    Check and return status of the service health
    """
    return GetHealthcheckResponse(status_code=200, content="OK")
