from domain.models.Bedroom import Bedroom
from domain.models.Guest import Guest

class Booking:
    def __init__(self,id_booking,guest: Guest,bedroom : Bedroom,start_date,end_date,total):
        self._id_booking = id_booking
        self._guest = guest
        self._bedroom = bedroom
        self._start_date=start_date
        self._end_date = end_date
        self._total = total

    @property
    def id_booking(self):
        return self._id_booking

    @id_booking.setter
    def id_booking(self, id_booking):
        self._id_booking = id_booking

    @property
    def guest(self):
        return self._guest

    @guest.setter
    def guest(self, guest: Guest):
        self._guest = guest

    @property
    def bedroom(self):
        return self._bedroom

    @bedroom.setter
    def bedroom(self, bedroom: Bedroom):
        self._bedroom = bedroom

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total