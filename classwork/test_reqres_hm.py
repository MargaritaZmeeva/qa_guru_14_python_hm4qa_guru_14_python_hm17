import json

import requests
from jsonschema import validate
from schemas import post_users, get_body_data

URL = "https://reqres.in/api/users"


def test_get():
    response = requests.get(URL + "/2")
    get_body = response.json()

    assert response.status_code == 200
    validate(get_body, schema=get_body_data)
