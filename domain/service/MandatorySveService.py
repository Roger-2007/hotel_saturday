from repository.persistence.MandatoryServiceRepository import MandatoryServiceRepository

class MandatorySveService:
    def __init__(self):
        self.mandatory_service_repository = MandatoryServiceRepository()

    def create_mandatory_sve_service(self, mandatory_service, db):
        try:
            self.mandatory_service_repository.create_mandatory_service_repository(mandatory_service,db)
            print("\nSe creo el servicio oblitatorio correctamente\n")
        except Exception as e:
            print(f"\nOcurrió un error al crear el servicio obligatorio: {e}\n")


    def all_mandatory_sve_service(self, db):
        try:
            resultado = self.mandatory_service_repository.all_mandatory_service_repository(db)
            if resultado:
                return resultado
            else:
                print("\nNo hay ningun servicio obligatorio creado\n")
        except Exception as e:
            print(f"\nOcurrió un error al traer los servicios obligatorios: {e}\n")

    def update_mandatory_sve_service(self, mandatory_service, db):
        try:
            self.mandatory_service_repository.update_mandatory_service_repository(mandatory_service,db)
            print("\nSe actualizo el servicio obligatorio correctamente\n")
        except Exception as e:
            print(f"\nOcurrió un error al actualizar el servicio obligatorio: {e}\n")

    def delete_mandatory_sve_service(self, mandatory_service, db):
        try:
            self.mandatory_service_repository.delete_mandatory_service_repository(mandatory_service, db)
            print("\nSe elimino el servicio obligatorio correctamente\n")
        except Exception as e:
            print(f"\nOcurrió un error al eliminar el servicio obligatorio: {e}\n")

    def get_total_price_mandatory_sve_service(self, db):
        try:
            resultado = self.mandatory_service_repository.get_total_price_mandatory_service_repository(db)
            if resultado:
                return resultado
            else:
                print("\nNo hay ningun servicio obligatorio\n")
                return 0
        except Exception as e:
            print(f"\nOcurrió un error al traer el total de los servicios obligatorios: {e}\n")
