from models.bookings import CreateBookingResponse
from src.constant import BookingData


def test_create_booking_client(create_booking_client):
    try:
        parsed = CreateBookingResponse(**create_booking_client)
    except Exception as e:
        raise AssertionError(f"Структура ответа не соответствует данным {e}")

    assert parsed.booking.bookingdates.checkin == "2026-01-01"

    assert create_booking_client['booking']['firstname'] == BookingData.FIRSTNAME.value, (
        "Вернулось некорректное имя\n"
        f"Response: \n{create_booking_client}\n"
        f"Ожидаемое имя: \n{BookingData.FIRSTNAME}\n"
    )
    assert create_booking_client['booking']['lastname'] == BookingData.LASTNAME.value, (
        "Вернулось некорректное имя\n"
        f"Response: \n{create_booking_client}\n"
        f"Ожидаемое имя: \n{BookingData.LASTNAME}\n"
    )
    print()
    print(create_booking_client)


def test_update_booking_client(booking_client, create_booking_client, auth_token, headers, valid_booking_payload):
    booking_id = create_booking_client["bookingid"]
    headers.update({"Cookie": f"token={auth_token}"})
    payload = valid_booking_payload.build()
    payload.update({"firstname": BookingData.UPDATE_FIRSTNAME.value})
    update_response = booking_client.update_booking(booking_id, headers, valid_booking_payload.build())
    print()
    print(update_response.json())