class Booking:
    def __init__(self,id_booking,id_guest,id_bedroom,start_date,end_date,total):
        self._id_booking = id_booking
        self._id_guest = id_guest
        self._id_bedroom = id_bedroom
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
    def id_guest(self):
        return self._id_guest

    @id_guest.setter
    def id_guest(self, id_guest):
        self._id_guest = id_guest

    @property
    def id_bedroom(self):
        return self._id_bedroom

    @id_bedroom.setter
    def id_bedroom(self, id_bedroom):
        self._id_bedroom = id_bedroom

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