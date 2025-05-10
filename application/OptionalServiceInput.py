from domain.models.OptionalService import OptionalService
from domain.service.OptionalSveService import OptionalSveService
import re

class OptionalServiceInput:

    def __init__(self):
        self.optional_service = OptionalService(None,None,None,None)
        self.optional_sve_service = OptionalSveService()

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
        self.optional_sve_service.create_optional_sve_service(self.optional_service,db)

    def all_optional_service(self,db):
        return self.optional_sve_service.all_optional_sve_service(db)

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
        self.optional_sve_service.update_optional_sve_service(self.optional_service,db)

    def delete_optional_service(self,id,db):
        self.optional_service.id=id
        self.optional_sve_service.delete_optional_sve_service(self.optional_service,db)
