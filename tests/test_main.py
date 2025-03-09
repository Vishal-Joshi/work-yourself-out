import pytest
from fastapi.testclient import TestClient
import uuid
from workoutplanner.main import app

# Create a test client
client = TestClient(app)


def test_create_workout():
    """Tests that create endpoint returns a valid UUID"""
    response = client.get("/create")

    assert response.status_code == 200
