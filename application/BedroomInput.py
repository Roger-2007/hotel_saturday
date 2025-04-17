from domain.models.Bedroom import Bedroom
from repository.persistence.BedroomRepository import BedroomRepository


class BedroomInput:
    def __init__(self):
        self.bedroom = Bedroom(None, None, None, None, None, None)
        self.bedroomRepository = BedroomRepository()

    def create_bedroom(self, db):
        number = int(input("Ingrese el numero de la habitacion"))
        self.bedroom.number = number
        type = input("Ingrese el tipo de habitacion")
        self.bedroom.type = type
        price = int(input("Ingrese el precio de la habitacion"))
        self.bedroom.price = price
        capacity = int(input("Ingrese la capacidad de la habitacion"))
        self.bedroom.capacity = capacity
        description = input("Ingrese la descripcion de la habitacion")
        self.bedroom.description = description
        status = int(input("Ingrese el estado de la habitacion"))
        self.bedroom.status = status
        self.bedroomRepository.create_bedroom_repository(self.bedroom,db)
