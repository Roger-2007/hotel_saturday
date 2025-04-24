from domain.models.Reservacion_ServicioOpcional import Reservacion_ServicioOpcional
from repository.persistence.Reservacion_ServicioOpcionalRepository import Reservacion_ServicioOpcionalRepository
class Reservacion_ServicioOpcionalInput:
    def __init__(self):
        self.reservacion_servicio_opcional = Reservacion_ServicioOpcional(None,None)
        self.reservacion_servicio_opcional_repository = Reservacion_ServicioOpcionalRepository()

    def create_reservacion_servicio_opcional(self,id_booking,id_optional_service,db):
        self.reservacion_servicio_opcional.id_booking=id_booking
        self.reservacion_servicio_opcional.id_optional_service=id_optional_service
        self.reservacion_servicio_opcional_repository.create_reservacion_servicioOpcional_repository(self.reservacion_servicio_opcional,db)
    