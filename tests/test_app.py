from src import app as app_module


def test_get_activities_returns_available_activities(client):
    activity_name = "Chess Club"

    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()
    assert activity_name in payload
    assert payload[activity_name]["participants"][0] == "michael@mergington.edu"


def test_signup_adds_participant_to_activity(client):
    activity_name = "Chess Club"
    email = "student@example.com"

    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    assert response.status_code == 200
    assert email in app_module.activities[activity_name]["participants"]


def test_duplicate_signup_is_rejected(client):
    activity_name = "Chess Club"
    email = "student@example.com"
    client.post(f"/activities/{activity_name}/signup", params={"email": email})

    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up for this activity"


def test_unregister_participant_removes_email_from_activity(client):
    activity_name = "Chess Club"
    email = "student@example.com"
    client.post(f"/activities/{activity_name}/signup", params={"email": email})

    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 200
    assert email not in app_module.activities[activity_name]["participants"]
