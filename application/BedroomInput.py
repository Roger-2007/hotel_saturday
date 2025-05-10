from domain.models.Bedroom import Bedroom
from domain.service.BedroomService import BedroomService
import re


class BedroomInput:
    def __init__(self):
        self.bedroom = Bedroom(None, None, None, None, None, None)
        self.bedroom_service = BedroomService()

    def create_bedroom(self, db):
        while True:
            try:
                type = input("Ingrese el tipo de habitacion")
                es_valido = re.fullmatch(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",type)
                if es_valido:
                    self.bedroom.type = type
                    break
                else:
                    print("\nSolo se permiten letras\n")
            except Exception as e:
                print(f"Ocurrió un error al escribir el tipo: {e}")

        while True:
            try:
                price = int(input("Ingrese el precio de la habitacion"))
                texto = str(price)
                es_valido = re.fullmatch(r"\d{5,8}",texto)
                if es_valido:
                    self.bedroom.price = price
                    break
                else:
                    print("El precio debe contener entre 5 a 8 digitos")
            except ValueError:
                print("El precio solo puede ser numeros")
            except Exception as e:
                print(f"Ocurrió un error al digitar el precio: {e}")
        while True:
            try:
                capacity = int(input("Ingrese la capacidad de la habitacion"))
                texto = str(capacity)
                es_valido = re.fullmatch(r"\d{1,2}",texto)
                if es_valido:
                    self.bedroom.capacity = capacity
                    break
                else:
                    print("\nSolo se puede entre 1 a 2 digitos\n")
            except ValueError:
                print("\nSolo se permiten numeros\n")
            except Exception as e:
                print(f"\nOcurró un error al ingresar la capacidad: {e}\n")

        while True:
            try:
                description = input("Ingrese la descripcion de la habitacion")
                es_valido = re.fullmatch(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",description)
                if es_valido:
                    self.bedroom.description = description
                    break
                else:
                    print("\nLa descripcion solo puede contener letras\n")
            except Exception as e:
                print(f"Ocurrió un error al ingresar la descripcion: {e}")

        self.bedroom_service.create_bedroom_service(self.bedroom,db)

    def update_bedroom(self,id_bedroom,db):
        self.bedroom.id_bedroom=id_bedroom
        while True:
            try:
                type = input("Ingrese el tipo de habitacion")
                es_valido = re.fullmatch(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",type)
                if es_valido:
                    self.bedroom.type = type
                    break
                else:
                    print("\nSolo se permiten letras\n")
            except Exception as e:
                print(f"Ocurrió un error al escribir el tipo: {e}")

        while True:
            try:
                price = int(input("Ingrese el precio de la habitacion"))
                texto = str(price)
                es_valido = re.fullmatch(r"\d{5,8}",texto)
                if es_valido:
                    self.bedroom.price = price
                    break
                else:
                    print("El precio debe contener entre 5 a 8 digitos")
            except ValueError:
                print("El precio solo puede ser numeros")
            except Exception as e:
                print(f"Ocurrió un error al digitar el precio: {e}")
        while True:
            try:
                capacity = int(input("Ingrese la capacidad de la habitacion"))
                texto = str(capacity)
                es_valido = re.fullmatch(r"\d{1,2}",texto)
                if es_valido:
                    self.bedroom.capacity = capacity
                    break
                else:
                    print("\nSolo se puede entre 1 a 2 digitos\n")
            except ValueError:
                print("\nSolo se permiten numeros\n")
            except Exception as e:
                print(f"\nOcurró un error al ingresar la capacidad: {e}\n")

        while True:
            try:
                description = input("Ingrese la descripcion de la habitacion")
                es_valido = re.fullmatch(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]",description)
                if es_valido:
                    self.bedroom.description = description
                    break
                else:
                    print("\nLa descripcion solo puede contener letras\n")
            except Exception as e:
                print(f"Ocurrió un error al ingresar la descripcion: {e}")
        self.bedroom_service.update_bedroom_service(self.bedroom,db)

    def all_bedrooms(self,db):
        return self.bedroom_service.all_bedrooms_service(db)

    def disable_bedroom(self,id_bedroom,db):
        self.bedroom.id_bedroom=id_bedroom
        self.bedroom_service.disable_bedroom_service(self.bedroom,db)
