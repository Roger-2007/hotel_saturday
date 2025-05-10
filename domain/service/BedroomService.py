from repository.persistence.BedroomRepository import BedroomRepository
from domain.models.Bedroom import Bedroom

class BedroomService:
    def __init__(self):
        self.bedroom = Bedroom(None,None,None,None,None,None)
        self.bedroom_repository = BedroomRepository()

    def create_bedroom_service(self,bedroom,db):
        try:
            self.bedroom_repository.create_bedroom_repository(bedroom,db)
            print("\nSe creo la habitacion correctamente\n")
        except Exception as e:
            print(f"\nOcurrió un error al crear la habitacion: {e}\n")

    def update_bedroom_service(self,bedroom,db):
        try:
            self.bedroom_repository.update_bedroom_repository(bedroom,db)
            print("Se actualizo la habitacion correctamente")
        except Exception as e:
            print(f"Ocurrió un error al actualizar la habitacion: {e}")

    def all_bedrooms_service(self,db):
        try:
            resultados = self.bedroom_repository.all_bedrooms_repository(db)
            if not resultados:
                print("\nLo sentimos, pero no hay ninguna habitacion disponible\n")
                return resultados
            else:
                return resultados
        except Exception as e:
            print(f"Ocurrió un error al listar las habitaciones: {e}")

    def disable_bedroom_service(self,bedroom,db):
        try:
            self.bedroom_repository.disable_bedroom_repository(bedroom,db)
        except Exception as e:
            print(f"Ocurrió un error al deshabilitar la habitacion: {e}")

