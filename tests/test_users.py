import pytest
from starlette import status

def test_delete_user_endpoint(authorized_client):
    response = authorized_client.post("/test_data/all")
    assert response.status_code == status.HTTP_200_OK
    response = authorized_client.delete("/users/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_create_user_endpoint_with_invalid_json_parameter(authorized_client):
    response = authorized_client.post("/users",
                           json={"subject": "testuser",
                                 "email": "test@example.com"})
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


if __name__ == "__main__":
    exit_code = pytest.main(["tests/", "-v"])
    print(f"Tests completed with exit code {exit_code}")