from domain.models.OptionalService import OptionalService

class OptionalServiceInput:

    def __init__(self):
        self.optional_service = OptionalService(None,None,None,None)

    def create_mandatory_service(self,db):
        id = int(input("Ingrese el id del servicio obligatorio"))
        self.optional_service.id=id
        name = input("Ingrese el nombre del servicio obligatorio")
        self.optional_service.name=name
        description = input("Ingrese al descripcion del servicio obligatorio")
        self.optional_service.description=description
        price = int(input("Ingrese el precio del servicio obligatorio"))
        self.optional_service.price=price
