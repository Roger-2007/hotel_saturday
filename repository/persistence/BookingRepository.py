from domain.models.Booking import Booking

class BookingRepository:
    def __init__(self):
        self.booking = Booking

    def create_booking_repository(self,booking,db):
        query = "INSERT INTO booking (id_booking,id_guest,id_bedroom,start_date,end_date,total) values (%s,%s,%s,%s,%s,%s)"
        values = (booking.id_booking,booking.id_guest,booking.id_bedroom,booking.start_date,booking.end_date,booking.total)
        db.execute_query(query,values)

    def get_id_booking_repository(self,booking,db):
        query = "SELECT id_booking from booking where id_guest =%s and id_bedroom = %s"
        values = (booking.id_guest,booking.id_bedroom)
        result = db.execute_query(query,values)
        return result

    def get_days_repository(self,booking,db):
        query = "SELECT datediff(end_date,start_date) from booking where id_booking = %s"
        values = (booking.id_booking,)
        result = db.execute_query(query,values)
        return result

    def get_total_price_optional_service_repository(self,booking,db):
        query = "select sum(price) from optionalservice where id_optionalService in (select id_optionalService from booking_optionalservice where id_booking = %s)"
        values = (booking.id_booking,)
        result = db.execute_query(query,values)
        return result

    def update_total_booking_repository(self,booking,db):
        query = "UPDATE booking set total=%s where id_booking=%s"
        values = (booking.total,booking.id_booking)
        db.execute_query(query,values)

