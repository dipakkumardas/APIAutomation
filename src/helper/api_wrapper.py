import requests
import json


def get_request(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:
        return response.json()
    return response


def generate_token(url, auth, headers, payload, in_json):
    response = requests.post(url=url, headers=headers, auth=auth, json=payload)
    if in_json is True:
        return response.json()
    return response


def post_request(url, auth, headers, payload, in_json):
    post_response_data = requests.post(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return post_response_data.json()
    return post_response_data


def patch_request(url, auth, headers, payload, in_json):
    patch_response_data = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


def delete_data(url, auth, headers, payload, in_json):
    delete_response_data = requests.delete(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data
