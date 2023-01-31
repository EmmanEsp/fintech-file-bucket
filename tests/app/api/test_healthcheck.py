"""
Testing Get Healthcheck endpoint
"""
from fastapi import status
from fastapi.testclient import TestClient


def test_get_healthcheck(client: TestClient):
    """
    Test: get healthcheck return status 200 content ok
    """
    raw_response = client.get("/healthcheck")

    response = raw_response.json()

    assert raw_response.status_code == status.HTTP_200_OK
    assert response["status_code"] == 200 and response["content"] == "OK"
