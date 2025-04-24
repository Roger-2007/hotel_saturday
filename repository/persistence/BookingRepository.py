from domain.models.Booking import Booking

class BookingRepository:
    def __init__(self):
        self.booking = Booking

    def create_booking(self,booking,db):
        query = "INSERT INTO booking (id_booking,id_guest,id_bedroom,start_date,end_date,total) values (%s,%s,%s,%s,%s,%s)"
        values =booking.id_booking,booking.id_guest,booking.id_bedroom,booking.start_date,booking.end_date,booking.total
        db.execute_query(query,values)


