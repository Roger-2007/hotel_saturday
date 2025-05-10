from repository.persistence.Reservacion_ServicioOpcionalRepository import Reservacion_ServicioOpcionalRepository

class BookingXOptSvcService:
    def __init__(self):
        self.booking_x_optSvc_repository=Reservacion_ServicioOpcionalRepository()
    def create_bookingXOptSvc(self,reservacion_servicio_opcional,db):
        try:
            self.booking_x_optSvc_repository.create_reservacion_servicioOpcional_repository(reservacion_servicio_opcional,db)
        except Exception as e:
            print(f"Ocurrió un error: {e}")
