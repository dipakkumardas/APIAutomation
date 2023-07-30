import pytest

# Payload
# Base URL
# Verify

from src.constains.apiconstains import *
from src.helper.api_wrapper import post_request, patch_request, generate_token
from src.helper.payload_manager import create_booking, update_booking, token_id
from src.helper.utils import common_headers, get_payload_auth, common_token_headers
from src.helper.common_verification import *


class TestIntregrationTC1(object):

    def test_verify_creating_booking_by_updating_deleting(self):
        print("\n **************Generate Token *****************")
        token_response = generate_token(url_create_token(), headers=common_headers(), auth=None, payload=token_id(),
                                        in_json=False)
        print(token_response.status_code)
        print(token_response.json())
        tokenid = token_response.json()['token']
        print("Token id is: ", tokenid)

        print("\n **************Create Booking *****************")

        response = post_request(url_create_booking(), auth=None, headers=common_headers(), payload=create_booking(),
                                in_json=False)
        print(response.status_code)
        print(response.json())
        verify_http_code(response, 200)
        booking_id = response.json()["bookingid"]
        print("The data type is :", type(booking_id))
        bookingno = str(booking_id)
        print("The data type is :", type(bookingno))
        print("Your Booking Is is:", booking_id)

        print("\n **************Update Booking *****************")

        # response = patch_request(url_update_booking(bookingno), auth=None, headers=common_token_headers(tokenid),
        #                          payload=update_booking(),
        #                          in_json=False)
        # print(response.status_code)
        # print(response.json())
