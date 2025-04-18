from domain.models.MandatoryService import MandatoryService

class MandatoryServiceInput:

    def __init__(self):
        self.mandatory_service = MandatoryService(None,None,None,None)

    def create_mandatory_service(self,db):
        id = int(input("Ingrese el id del servicio obligatorio"))
        self.mandatory_service.id=id
        name = input("Ingrese el nombre del servicio obligatorio")
        self.mandatory_service.name=name
        description = input("Ingrese al descripcion del servicio obligatorio")
        self.mandatory_service.description=description
        price = int(input("Ingrese el precio del servicio obligatorio"))
        self.mandatory_service.price=price
