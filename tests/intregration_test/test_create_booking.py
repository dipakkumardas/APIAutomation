import pytest

# Payload
# Base URL
# Verify

from src.constains.apiconstains import base_url, url_create_booking
from src.helper.api_wrapper import post_request
from src.helper.payload_manager import create_booking
from src.helper.utils import common_headers
from src.helper.common_verification import *


class TestIntregration(object):

    def test_create_booking_tc1(self):
        # headers = {
        #     "Content-Type": "application/json",
        # }

        response = post_request(url_create_booking(), auth=None, headers=common_headers(), payload=create_booking(),
                                in_json=False)
        print(response.status_code)
        print(response.json())
        verify_http_code(response, 200)
        # booking_id = response.json()["bookingid"]

        verify_key_for_not_null_grated_than_zero(response.json()["bookingid"])

    def test_create_booking_tc2(self):
        assert True == True

    def test_create_booking_tc3(self):
        assert True == True

# URL -> Separated URL
# Payload - Separated Payload manager
# Headers -> Headers Utils
# Verify - Separated Verify


