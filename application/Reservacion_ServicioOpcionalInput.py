from domain.models.Reservacion_ServicioOpcional import Reservacion_ServicioOpcional
from domain.service.BookingXOptSvcService import BookingXOptSvcService
class Reservacion_ServicioOpcionalInput:
    def __init__(self):
        self.reservacion_servicio_opcional = Reservacion_ServicioOpcional(None,None)
        self.bookingXOptSvcService = BookingXOptSvcService()

    def create_reservacion_servicio_opcional(self,id_booking,id_optional_service,db):
        self.reservacion_servicio_opcional.id_booking=id_booking
        self.reservacion_servicio_opcional.id_optional_service=id_optional_service
        self.bookingXOptSvcService.create_bookingXOptSvc(self.reservacion_servicio_opcional,db)
