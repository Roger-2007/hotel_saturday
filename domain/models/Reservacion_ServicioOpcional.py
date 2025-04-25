class Reservacion_ServicioOpcional:
    def __init__(self,id_booking,id_optional_service):
        self._id_booking=id_booking
        self._id_optional_service=id_optional_service

    @property
    def id_booking(self):
        return self._id_booking

    @id_booking.setter
    def id_booking(self, id_booking):
        self._id_booking = id_booking

    @property
    def id_optional_service(self):
        return self._id_optional_service

    @id_optional_service.setter
    def id_optional_service(self, id_optional_service):
        self._id_optional_service = id_optional_service