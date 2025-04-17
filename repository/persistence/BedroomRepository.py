from domain.models.Bedroom import Bedroom


class BedroomRepository:
    def __init__(self):
        self.bedroom = Bedroom

    def create_bedroom_repository(self, bedroom, db):
        query = "INSERT INTO bedroom (number,type,price,capacity,description,status) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (bedroom.number, bedroom.type, bedroom.price, bedroom.capacity, bedroom.description, bedroom.status)
        db.execute_query(query , values)
