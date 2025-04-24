class Reservacion_ServicioOpcionalRepository:
    def create_reservacion_servicioOpcional_repository(self,reservacion_servicio_opcional,db):
        query = "INSERT INTO booking_optionalservice (id_booking,id_optionalservice) values (%s,%s)"
        values = (reservacion_servicio_opcional.id_booking,reservacion_servicio_opcional.id_optionalservice)
        db.execute_query(query,values)