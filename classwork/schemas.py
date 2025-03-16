post_users_py = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "id": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "name": {
            "type": "string"
        }

    },
    "required": [
        "id",
        "createdAt",
        "job",
        "name"
    ]
}


get_body_data = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "email": {
      "type": "string"
    },
    "first_name": {
      "type": "string"
    },
    "last_name": {
      "type": "string"
    },
    "avatar": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "email",
    "first_name",
    "last_name",
    "avatar"
  ]
}