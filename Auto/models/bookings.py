from pydantic import BaseModel

from src.constant import BookingData
from typing import Optional

class BookingDates(BaseModel):
    checkin: str
    checkout: str

class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None

    def build(self):
        return self.model_dump()


class CreateBookingResponse(BaseModel):
    bookingid: int
    booking: Booking
