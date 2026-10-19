import pytest
from fastapi import status

def test_create_all_data_endpoint(unauthorized_client):
    response = unauthorized_client.post("/test_data/all")
    assert response.status_code == status.HTTP_200_OK
    response = unauthorized_client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 6

if __name__ == "__main__":
    exit_code = pytest.main(["tests/", "-v"])
    print(f"Tests completed with exit code {exit_code}")