import pytest
from fastapi.testclient import TestClient
from myapp.main import app

client = TestClient(app)


def test_read_env():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"

    # Add more assertions based on the expected behavior of the read_env endpoint


def test_update_env():
    # Assuming you have a dummy directory structure in the test_assets folder
    env_file_path = "tests/test_assets/dummy_dir/dummy_file.env"
    json_file_path = "tests/test_assets/dummy_dir/dummy_file.json"

    key = "DATABASE_HOST"
    value = "testdb.example.com"

    # Call the update_env endpoint with the test-specific env file path, key, and value
    response_env = client.post("/update", data={"file_path": env_file_path, "key": key, "value": value})

    # Assert the expected behavior based on the response or any side effects
    # ...

    key = "API_SECRET"
    value = "newsecret"

    # Call the update_env endpoint with the test-specific json file path, key, and value
    response_json = client.post("/update", data={"file_path": json_file_path, "key": key, "value": value})

    # Assert the expected behavior based on the response or any side effects
    # ...

    # Optionally, you can clean up the test assets after the test is complete
    # ...
