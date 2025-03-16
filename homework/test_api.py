import random
import string

import requests

from body_post import body_request_post, body_request_put_pet

url_pet = "https://petstore.swagger.io/v2/pet/"
url_user = "https://petstore.swagger.io/v2/user/"


def test_get():
    pet_id = '1'
    response = requests.get(url=url_pet + pet_id)
    response.body = response.json()

    assert response.body["id"] == int(pet_id)
    assert response.status_code == 200


def test_post():
    response = requests.post(url_user, json=body_request_post)
    assert response.json()["code"] == 200


def test_put():
    response = requests.put(url_pet, json=body_request_put_pet)

    assert response.json()["category"]["name"] == "dog"
    assert response.json()["category"]["name"] == body_request_put_pet["category"]["name"]


def test_delete():
    delete_name = "string"
    response = requests.delete(url=url_user + delete_name)
    assert response.status_code == 200


def test_delete_random_name():
    random_str = ''.join(random.choices(string.ascii_letters, k=4))
    response = requests.delete(url=url_user + random_str)
    assert response.status_code != 200
