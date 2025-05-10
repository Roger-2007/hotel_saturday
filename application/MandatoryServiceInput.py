from domain.models.MandatoryService import MandatoryService
from domain.service.MandatorySveService import MandatorySveService
import re

class MandatoryServiceInput:

    def __init__(self):
        self.mandatory_service = MandatoryService(None,None,None,None)
        self.mandatory_sve_service = MandatorySveService()
    def create_mandatory_service(self,db):
        while True:
            try:
                name = input("Ingrese el nombre del servicio obligatorio")
                es_valido = re.fullmatch(r"^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$",name)
                if es_valido:
                    self.mandatory_service.name=name
                    break
                else:
                    print("\nSolo se permiten letras\n")
            except Exception as e:
                print(f"\nOcurrió un error: {e}\n")

        while True:
            try:
                description = input("Ingrese al descripcion del servicio obligatorio")
                es_valido = re.fullmatch(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",description)
                if es_valido:
                    self.mandatory_service.description=description
                    break
                else:
                    print("\nLa descripcion solo puede contener letras\n")
            except Exception as e:
                print(f"Ocurrió un error al ingresar la descripcion: {e}")


        while True:
            try:
                price = int(input("Ingrese el precio del servicio obligatorio"))
                texto = str(price)
                es_valido = re.fullmatch(r"\d{4,6}",texto)
                if es_valido:
                    self.mandatory_service.price = price

                    break
                else:
                    print("El precio debe contener entre 4 a 6 digitos")
            except ValueError:
                print("El precio solo puede ser numeros")
            except Exception as e:
                print(f"Ocurrió un error al digitar el precio: {e}")
        self.mandatory_sve_service.create_mandatory_sve_service(self.mandatory_service,db)

    def all_mandatory_service(self,db):
        return self.mandatory_sve_service.all_mandatory_sve_service(db)

    def update_mandatory_service(self,id_mandatory_service,db):
        self.mandatory_service.id=id_mandatory_service
        while True:
            try:
                name = input("Ingrese el nombre del servicio obligatorio")
                es_valido = re.fullmatch(r"^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", name)
                if es_valido:
                    self.mandatory_service.name = name
                    break
                else:
                    print("\nSolo se permiten letras\n")
            except Exception as e:
                print(f"\nOcurrió un error: {e}\n")

        while True:
            try:
                description = input("Ingrese al descripcion del servicio obligatorio")
                es_valido = re.fullmatch(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", description)
                if es_valido:
                    self.mandatory_service.description = description
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
                    self.mandatory_service.price = price

                    break
                else:
                    print("El precio debe contener entre 4 a 6 digitos")
            except ValueError:
                print("El precio solo puede ser numeros")
            except Exception as e:
                print(f"Ocurrió un error al digitar el precio: {e}")
        self.mandatory_sve_service.update_mandatory_sve_service(self.mandatory_service, db)

    def delete_mandatory_service(self,id,db):
        self.mandatory_service.id=id
        self.mandatory_sve_service.delete_mandatory_sve_service(self.mandatory_service,db)

    def get_total_price_mandatory_service(self,db):
        return self.mandatory_sve_service.get_total_price_mandatory_sve_service(db)
