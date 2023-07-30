import json


def get_payload_auth():
    file_data = open("src/resources/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data


def common_headers():
    headers = {
        "Content-Type": "application/json",
    }
    return headers


def common_token_headers(token):
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token"
    }
    return headers
