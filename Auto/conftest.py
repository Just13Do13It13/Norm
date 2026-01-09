import pytest
import requests

from clients.booking_client import BookingClient
from models.bookings import BookingDates, Booking
from src.constant import BookingData
from src.settings import settings


@pytest.fixture(scope="session")
def booking_client():
    return BookingClient(base_url=settings.base_url)

@pytest.fixture(scope="session")
def valid_booking_payload():
    return Booking(
        firstname=BookingData.FIRSTNAME.value,
        lastname=BookingData.LASTNAME.value,
        totalprice=1000,
        depositpaid=True,
        bookingdates=BookingDates(
            checkin="2026-01-01",
            checkout="2026-01-01"
        ),
        additionalneeds="Breakfast"
    )

@pytest.fixture(scope="session")
def headers():
    return {'Content-Type': 'application/json'}


@pytest.fixture(scope="session")
def create_booking_client(booking_client, valid_booking_payload, headers):
    response = booking_client.create_booking(valid_booking_payload.build(), headers)
    data = response.json()
    yield data
    booking_client.delete_booking(data["bookingid"], headers)
    print(f"Удалили запись: {data['bookingid']}")

@pytest.fixture(scope="session")
def auth_token(booking_client):
   response = booking_client.get_token(
       login=settings.username,
       password=settings.password
   )
   data = response.json()
   print("AUTH RESPONSE:", data)
   token = data.get('token') or data.get('access_token')
   if not token:
       raise ValueError(f"Не удалось получить токен, ответ сервера: {data}")
   return token
