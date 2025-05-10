from domain.models.OptionalService import OptionalService
from repository.persistence.OptionalServiceRepository import OptionalServiceRepository
import re

class OptionalServiceInput:

    def __init__(self):
        self.optional_service = OptionalService(None,None,None,None)
        self.optional_service_repository = OptionalServiceRepository()

    def create_optional_service(self,db):

        while True:
            try:
                name = input("Ingrese el nombre del servicio obligatorio")
                es_valido = re.fullmatch(r"^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", name)
                if es_valido:
                    self.optional_service.name = name
                    break
                else:
                    print("\nSolo se permiten letras\n")
            except Exception as e:
                print(f"\nOcurrió un error: {e}\n")

        while True:
            try:
                description = input("Ingrese al descripcion del servicio obligatorio")
                es_valido = re.fullmatch(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]", description)
                if es_valido:
                    self.optional_service.description = description
                    break
                else:
                    print("\nLa descripcion solo puede contener letras\n")
            except Exception as e:
                print(f"Ocurrió un error al ingresar la descripcion: {e}")

        while True:
            try:
                price = int(input("Ingrese el precio del servicio obligatorio"))
                texto = str(price)
                es_valido = re.fullmatch(r"\d{4,6}", texto)
                if es_valido:
                    self.optional_service.price = price

                    break
                else:
                    print("El precio debe contener entre 4 a 6 digitos")
            except ValueError:
                print("El precio solo puede ser numeros")
            except Exception as e:
                print(f"Ocurrió un error al digitar el precio: {e}")
        self.optional_service_repository.create_optional_service_repository(self.optional_service,db)

    def all_optional_service(self,db):
        return self.optional_service_repository.all_optional_service_repository(db)

    def update_optional_service(self,id,db):
        self.optional_service.id=id
        while True:
            try:
                name = input("Ingrese el nombre del servicio obligatorio")
                es_valido = re.fullmatch(r"^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", name)
                if es_valido:
                    self.optional_service.name = name
                    break
                else:
                    print("\nSolo se permiten letras\n")
            except Exception as e:
                print(f"\nOcurrió un error: {e}\n")

        while True:
            try:
                description = input("Ingrese al descripcion del servicio obligatorio")
                es_valido = re.fullmatch(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]", description)
                if es_valido:
                    self.optional_service.description = description
                    break
                else:
                    print("\nLa descripcion solo puede contener letras\n")
            except Exception as e:
                print(f"Ocurrió un error al ingresar la descripcion: {e}")

        while True:
            try:
                price = int(input("Ingrese el precio del servicio obligatorio"))
                texto = str(price)
                es_valido = re.fullmatch(r"\d{4,6}", texto)
                if es_valido:
                    self.optional_service.price = price

                    break
                else:
                    print("El precio debe contener entre 4 a 6 digitos")
            except ValueError:
                print("El precio solo puede ser numeros")
            except Exception as e:
                print(f"Ocurrió un error al digitar el precio: {e}")
        self.optional_service_repository.update_optional_service_repository(self.optional_service,db)

    def delete_optional_service(self,id,db):
        self.optional_service.id=id
        self.optional_service_repository.delete_optional_service_repository(self.optional_service,db)
