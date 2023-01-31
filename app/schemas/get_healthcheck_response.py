"""
Get Healthcheck endpoint response schema
"""
from pydantic import BaseModel


class GetHealthcheckResponse(BaseModel):
    """
    Response for get healthcheck endpoint
    """

    status_code: int
    content: str
