from repository.persistence.OptionalServiceRepository import OptionalServiceRepository

class OptionalSveService:
    def __init__(self):
        self.optional_service_repository = OptionalServiceRepository()

    def create_optional_sve_service(self, mandatory_service, db):
        try:
            self.optional_service_repository.create_optional_service_repository(mandatory_service,db)
            print("\nSe creo el servicio opcional correctamente\n")
        except Exception as e:
            print(f"\nOcurrió un error al crear el servicio opcional: {e}\n")


    def all_optional_sve_service(self, db):
        try:
            resultado = self.optional_service_repository.all_optional_service_repository(db)
            if resultado:
                return resultado
            else:
                print("\nNo hay ningun servicio opcional creado\n")
        except Exception as e:
            print(f"\nOcurrió un error al traer los servicios opcionales: {e}\n")

    def update_optional_sve_service(self, mandatory_service, db):
        try:
            self.optional_service_repository.update_optional_service_repository(mandatory_service,db)
            print("\nSe actualizo el servicio opcional correctamente\n")
        except Exception as e:
            print(f"\nOcurrió un error al actualizar el servicio opcional: {e}\n")

    def delete_optional_sve_service(self, mandatory_service, db):
        try:
            self.optional_service_repository.delete_optional_service_repository(mandatory_service, db)
            print("\nSe elimino el servicio opcional correctamente\n")
        except Exception as e:
            print(f"\nOcurrió un error al eliminar el servicio opcional: {e}\n")


