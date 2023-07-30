def create_booking():
    payload = {
        "firstname": "David",
        "lastname": "Brown",
        "totalprice": 9999,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-02"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def update_booking():
    payload = {
        "firstname": "Jems",
        "lastname": "Miller",
        "totalprice": 3000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-07-30",
            "checkout": "2023-07-31"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def token_id():

    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload
