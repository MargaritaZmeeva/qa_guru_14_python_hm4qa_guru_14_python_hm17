import random
import string
import requests
import pytest

url = "https://reqres.in/api/users"
user_id = 2


@pytest.fixture
def random_user():
    length = random.randint(5, 10)
    name = ''.join(random.choices(string.ascii_letters, k=length))
    job = ''.join(random.choices(string.ascii_letters, k=length))
    return {"name": name, "job": job}


def test_create_user(random_user):
    response = requests.post(url, json=random_user)
    response_json = response.json()

    assert response.status_code == 201
    assert response_json["name"] == random_user["name"]
    assert response_json["job"] == random_user["job"]


def test_get_user():
    response = requests.get(url=f"{url}/{user_id}")
    response_json = response.json()

    assert response.status_code == 200
    assert "id" in response_json['data']
    assert "email" in response_json['data']
    assert "first_name" in response_json["data"]


def test_delete_user():
    response = requests.delete(url=f"{url}/{user_id}")

    assert response.status_code == 204
