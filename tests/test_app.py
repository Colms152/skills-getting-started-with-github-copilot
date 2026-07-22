from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "student@example.com"

    client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert email in activities[activity_name]["participants"]

    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]
