import pytest
from fastapi import status

def test_create_all_data(unauthorized_client):
    response = unauthorized_client.post("/test_data/all")
    assert response.status_code == status.HTTP_200_OK
    response = unauthorized_client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 6

def test_delete_user_endpoint(authorized_client):
    response = authorized_client.post("/test_data/all")
    assert response.status_code == status.HTTP_200_OK
    response = authorized_client.delete("/users/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT






if __name__ == "__main__":
    exit_code = pytest.main(["tests/", "-v"])
    print(f"Tests completed with exit code {exit_code}")