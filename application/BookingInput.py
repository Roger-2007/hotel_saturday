from domain.models.Booking import Booking
from domain.service.BookingService import BookingService
import re


class BookingInput:
    def __init__(self):
        self.booking = Booking(None, None, None, None, None, None)
        self.booking_service = BookingService()

    def create_booking(self, id_guest, id_bedroom, db):
        self.booking.id_guest = id_guest
        self.booking.id_bedroom = id_bedroom
        while True:
            while True:
                try:
                    start_date = input("Ingrese la fecha de inicio: YYYY-MM-DD")
                    es_valido = re.fullmatch(r"^20\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$", start_date)
                    if es_valido:
                        self.booking.start_date = start_date
                        break
                    else:
                        print(
                            "La fecha de inicio de ser: año de 4 digitos, guion, mes de 2 digitos, guion, dia de 2 digitos\nEjemplos:\n2025-11-03\n2025-02-20")
                except Exception as e:
                    print(f"Ocurrió un error al ingresar la fecha de inicio: {e}")
            while True:
                try:
                    end_date = input("Ingrese la fecha de fin: YYYY-MM-DD")
                    es_valido = re.fullmatch(r"^20\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$", end_date)
                    if es_valido:
                        self.booking.end_date = end_date
                        break
                    else:
                        print(
                            "La fecha de fin de ser: año de 4 digitos, guion, mes de 2 digitos, guion, dia de 2 digitos\nEjemplos:\n2025-11-03\n2025-02-20")
                except Exception as e:
                    print(f"Ocurrió un error al ingresar la fecha de fin: {e}")
            if self.booking.start_date>self.booking.end_date:
                print("La fecha de fin no puede ser inferior a la fecha de inicio")
            else:
                break
        self.booking.total = 0
        self.booking_service.create_booking_service(self.booking, db)

    def get_id_booking(self, id_guest, id_bedroom, db):
        self.booking.id_guest = id_guest
        self.booking.id_bedroom = id_bedroom
        return self.booking_service.get_id_booking_service(self.booking, db)

    def get_days(self, id_booking, db):
        self.booking.id_booking = id_booking
        return self.booking_service.get_days_service(self.booking, db)

    def get_total_price_optional_service(self, id_booking, db):
        self.booking.id_booking = id_booking
        return self.booking_service.get_total_price_optional_service_service(self.booking, db)

    def update_total_booking(self, id_booking, total, db):
        self.booking.id_booking = id_booking
        self.booking.total = total
        self.booking_service.update_total_booking_service(self.booking, db)
