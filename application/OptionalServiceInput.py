from domain.models.OptionalService import OptionalService
from repository.persistence.OptionalServiceRepository import OptionalServiceRepository

class OptionalServiceInput:

    def __init__(self):
        self.optional_service = OptionalService(None,None,None,None)
        self.optional_service_repository = OptionalServiceRepository()

    def create_optional_service(self,db):

        name = input("Ingrese el nombre del servicio opcional")
        self.optional_service.name=name
        description = input("Ingrese al descripcion del servicio opcional")
        self.optional_service.description=description
        price = int(input("Ingrese el precio del servicio opcional"))
        self.optional_service.price=price
        self.optional_service_repository.create_optional_service_repository(self.optional_service,db)

    def all_optional_service(self,db):
        return self.optional_service_repository.all_optional_service_repository(db)

    def update_optional_service(self,db):
        name = input("Ingrese el nombre del servicio opcional")
        self.optional_service.name = name
        description = input("Ingrese al descripcion del servicio opcional")
        self.optional_service.description = description
        price = int(input("Ingrese el precio del servicio opcional"))
        self.optional_service.price = price
        self.optional_service_repository.update_optional_service_repository(self.optional_service,db)

    def delete_optional_service(self,id,db):
        self.optional_service.id=id
        self.optional_service_repository.delete_optional_service_repository(self.optional_service,db)
