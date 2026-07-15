from fastapi.testclient import TestClient


# ---------------------------------------------------------------------------
# GET /
# ---------------------------------------------------------------------------

def test_root_redirects_to_index(client: TestClient):
    # Arrange — no preconditions needed

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


# ---------------------------------------------------------------------------
# GET /activities
# ---------------------------------------------------------------------------

def test_get_activities_returns_200(client: TestClient):
    # Arrange — activities are pre-seeded by the app

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_all_activities(client: TestClient):
    # Arrange — activities are pre-seeded by the app

    # Act
    response = client.get("/activities")

    # Assert
    data = response.json()
    assert len(data) == 11


def test_get_activities_each_has_required_fields(client: TestClient):
    # Arrange — activities are pre-seeded by the app

    # Act
    response = client.get("/activities")

    # Assert
    required_fields = {"description", "schedule", "max_participants", "participants"}
    for name, details in response.json().items():
        assert required_fields.issubset(details.keys()), f"{name} is missing required fields"


# ---------------------------------------------------------------------------
# POST /activities/{activity_name}/signup
# ---------------------------------------------------------------------------

def test_signup_success(client: TestClient):
    # Arrange — Soccer Team has no participants, email is new
    activity_name = "Soccer Team"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert email in response.json()["message"]


def test_signup_adds_participant(client: TestClient):
    # Arrange — Soccer Team has no participants
    activity_name = "Soccer Team"
    email = "newstudent@mergington.edu"

    # Act
    client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]
    assert email in participants


def test_signup_duplicate_returns_400(client: TestClient):
    # Arrange — sign up the student first so they are already a participant
    activity_name = "Soccer Team"
    email = "dup@mergington.edu"
    client.post(f"/activities/{activity_name}/signup?email={email}")

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 400


def test_signup_unknown_activity_returns_404(client: TestClient):
    # Arrange — use an activity name that does not exist

    # Act
    response = client.post("/activities/Nonexistent Club/signup?email=x@mergington.edu")

    # Assert
    assert response.status_code == 404


# ---------------------------------------------------------------------------
# DELETE /activities/{activity_name}/participants
# ---------------------------------------------------------------------------

def test_unregister_success(client: TestClient):
    # Arrange — sign up a student so they can be removed
    activity_name = "Soccer Team"
    email = "leaving@mergington.edu"
    client.post(f"/activities/{activity_name}/signup?email={email}")

    # Act
    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    # Assert
    assert response.status_code == 200
    assert email in response.json()["message"]


def test_unregister_removes_participant(client: TestClient):
    # Arrange — sign up a student so they appear in participants
    activity_name = "Soccer Team"
    email = "leaving@mergington.edu"
    client.post(f"/activities/{activity_name}/signup?email={email}")

    # Act
    client.delete(f"/activities/{activity_name}/participants?email={email}")

    # Assert
    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]
    assert email not in participants


def test_unregister_not_signed_up_returns_404(client: TestClient):
    # Arrange — email was never signed up for the activity

    # Act
    response = client.delete("/activities/Soccer Team/participants?email=ghost@mergington.edu")

    # Assert
    assert response.status_code == 404


def test_unregister_unknown_activity_returns_404(client: TestClient):
    # Arrange — use an activity name that does not exist

    # Act
    response = client.delete("/activities/Nonexistent Club/participants?email=x@mergington.edu")

    # Assert
    assert response.status_code == 404
