from domain.models.MandatoryService import MandatoryService
from repository.persistence.MandatoryServiceRepository import MandatoryServiceRepository

class MandatoryServiceInput:

    def __init__(self):
        self.mandatory_service = MandatoryService(None,None,None,None)
        self.mandatory_service_repository = MandatoryServiceRepository()

    def create_mandatory_service(self,db):

        name = input("Ingrese el nombre del servicio obligatorio")
        self.mandatory_service.name=name
        description = input("Ingrese al descripcion del servicio obligatorio")
        self.mandatory_service.description=description
        price = int(input("Ingrese el precio del servicio obligatorio"))
        self.mandatory_service.price=price
        self.mandatory_service_repository.create_mandatory_service_repository(self.mandatory_service,db)

    def all_mandatory_service(self,db):
        return self.mandatory_service_repository.all_mandatory_service_repository(db)

    def update_mandatory_service(self,db):
        name = input("Ingrese el nombre del servicio obligatorio")
        self.mandatory_service.name = name
        description = input("Ingrese al descripcion del servicio obligatorio")
        self.mandatory_service.description = description
        price = int(input("Ingrese el precio del servicio obligatorio"))
        self.mandatory_service.price = price
        self.mandatory_service_repository.update_mandatory_service_repository(self.mandatory_service,db)

    def delete_mandatory_service(self,id,db):
        self.mandatory_service.id=id
        self.mandatory_service_repository.delete_mandatory_service_repository(self.mandatory_service,db)

    def get_total_price_mandatory_service(self,db):
        return self.mandatory_service_repository.get_total_price_mandatory_service_repository(db)
