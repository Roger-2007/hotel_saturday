from domain.models.Bedroom import Bedroom
from repository.persistence.BedroomRepository import BedroomRepository


class BedroomInput:
    def __init__(self):
        self.bedroom = Bedroom(None, None, None, None, None, None)
        self.bedroomRepository = BedroomRepository()

    def create_bedroom(self, db):

        type = input("Ingrese el tipo de habitacion")
        self.bedroom.type = type
        price = int(input("Ingrese el precio de la habitacion"))
        self.bedroom.price = price
        capacity = int(input("Ingrese la capacidad de la habitacion"))
        self.bedroom.capacity = capacity
        description = input("Ingrese la descripcion de la habitacion")
        self.bedroom.description = description

        self.bedroomRepository.create_bedroom_repository(self.bedroom,db)

    def all_bedrooms(self,db):
        return self.bedroomRepository.all_bedrooms_repository(db)

    def disable_bedroom(self,id_bedroom,db):
        self.bedroom.id_bedroom=id_bedroom
        self.bedroomRepository.disable_bedroom_repository(self.bedroom,db)
