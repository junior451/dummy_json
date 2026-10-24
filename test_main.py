from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_users():
    response = client.get("/users")
    assert response.status_code == 200

    data = response.json()

    assert "total" in data
    assert "count" in data
    assert "users" in data

    assert data["total"] == 208
    assert data["count"] == 208

    assert data["users"][0] == {
            "id": 1,
            "firstName": "Emily",
            "lastName": "Johnson",
            "email": "emily.johnson@x.dummyjson.com",
            "phone": "+81 965-431-3024"
    }

    assert data["users"][-1] == {
            "id": 208,
            "firstName": "Samantha",
            "lastName": "Martinez",
            "email": "samantha.martinez@x.dummyjson.com",
            "phone": "+49 493-402-2473"
  }


def test_valid_first_name_filter():
  response = client.get("/users?firstName=Emily")

  assert response.status_code == 200

  data = response.json()

  assert data["total"] == 208
  assert data["count"] == 2

  assert data["users"][0] == {
          "id": 1,
          "firstName": "Emily",
          "lastName": "Johnson",
          "email": "emily.johnson@x.dummyjson.com",
          "phone": "+81 965-431-3024"
  }

def test_invalid_first_name_filter():
  response = client.get("/users?firstName=Jamie")
  assert response.status_code == 200

  data = response.json()

  assert data["total"] == 208
  assert data["count"] == 0

  assert data["users"] == []

def test_valid_last_name_filter():
  response = client.get("/users?lastName=Johnson")

  assert response.status_code == 200

  data = response.json()

  assert data["total"] == 208
  assert data["count"] == 2

  assert data["users"][0] == {
          "id": 1,
          "firstName": "Emily",
          "lastName": "Johnson",
          "email": "emily.johnson@x.dummyjson.com",
          "phone": "+81 965-431-3024"
  }
  

def test_invalid_first_name_or_last_name_filter():
  response = client.get("/users?firstName=Albert&lastName=Smith")
  
  assert response.status_code == 200

  data = response.json()

  assert data["total"] == 208
  assert data["count"] == 0

  assert data["users"] == []


def test_invalid_path():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}