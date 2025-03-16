import json

import requests
from jsonschema import validate
from schemas import post_users_py

url = "https://reqres.in/api/users"
payload = {"name": "morpheus", "job": "leader"}

# response = requests.request("POST", url, data=payload)
# print(response.text) # вариант_1

# response = requests.post(url, data=payload)
# print(response.text)  # вариант_2


post_users = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "createdAt"
    ]
}


def test_status_code():
    response = requests.post(url, data=payload)
    assert response.status_code == 201


def test_schema_validate_from_file():
    response_from_file = requests.post(url, data={"name": "morpheus", "job": "leader"})
    body_from_file = response_from_file.json()
    with open("post_users.json") as file:  # открываем файл
        validate(body_from_file,
                 schema=json.loads(file.read()))  # file.read возвращает строку, а нам нужен конверт в json


def test_schema_validate_from_var():
    response_from_var = requests.post(url, data={"name": "morpheus", "job": "leader"})
    body_from_var = response_from_var.json()
    validate(body_from_var, schema=post_users)  # можно добавить переменную с ответом в .ру файл и импортнуть файл


def test_schema_validate_from_py():
    response = requests.post(url, data={"name": "morpheus", "job": "leader"})
    body_from_py = response.json()
    validate(body_from_py, schema=post_users_py)


def test_job_name_returns():
    job = 'qa'
    response = requests.post(url, data={"name": "morpheus", "job": job})
    body = response.json()
    print(body)

    assert body["job"] == job


def test_get_with_params():
    # response = requests.get("https://reqres.in/api/users?page=2&per_pages=4") #плохая запись, урл склеян из параметров
    response = requests.get(
        url="https://reqres.in/api/users",
        params={"page": 1, "per_page": 4}
    )
    ids = [element["id"] for element in response.json()["data"]]
    # ids - список. сравниваем кол-во уникальных элементов в списке,
    # преобразуя его в кортеж
    set_ids = set(ids)
    assert len(set_ids) == len(ids)
