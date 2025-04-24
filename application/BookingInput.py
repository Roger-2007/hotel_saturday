from domain.models.Booking import Booking
from repository.persistence.BookingRepository import BookingRepository
class BookingInput:
    def __init__(self):
        self.booking = Booking(None,None,None,None,None,None)
        self.booking_repository = BookingRepository()

    def create_booking(self,id_guest,id_bedroom,total,db):
        self.booking.id_guest=id_guest
        self.booking.id_bedroom=id_bedroom
        start_date = input("Ingrese la fecha de inicio: YYYY-MM-DD")
        self.booking.start_date=start_date
        end_date = input("Ingrese la fecha de fin: YYYY-MM-DD")
        self.booking.end_date=end_date
        self.booking.total=total
        self.booking_repository.create_booking_repository(self.booking,db)





