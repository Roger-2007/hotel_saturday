from repository.persistence.BookingRepository import BookingRepository

class BookingService:
    def __init__(self):
        self.booking_repository = BookingRepository()

    def create_booking_service(self,booking,db):
        try:
            self.booking_repository.create_booking_repository(booking,db)
            print("Se creó la reservacion correctamente")
        except Exception as e:
            print(f"Ocurrió un error al hacer la reservacion: {e}")

    def get_id_booking_service(self,booking,db):
        try:
            resultado = self.booking_repository.get_id_booking_repository(booking,db)
            return resultado
        except Exception as e:
            print(f"Ocurrió un erro al traer la id de la reservacion: {e}")

    def get_days_service(self, booking, db):
        try:
            resultado = self.booking_repository.get_days_repository(booking,db)
            if resultado:
                return resultado
            else:
                return 1
        except Exception as e:
            print(f"Ocurrió un error al traer los dias: {e}")

    def get_total_price_optional_service_service(self, booking, db):
        try:
            resultado = self.booking_repository.get_total_price_optional_service_repository(booking,db)
            return resultado
        except Exception as e:
            print(f"Ocurrió un error al traer el precio total de los servicios opcionales: {e}")

    def update_total_booking_service(self,booking,db):
        try:
            self.booking_repository.update_total_booking_repository(booking,db)
        except Exception as e:
            print(f"Ocurrió un error al actualizar el precio de la reservacion: {e}")
