from domain.models.Bedroom import Bedroom


class BedroomRepository:
    def __init__(self):
        self.bedroom = Bedroom

    def create_bedroom_repository(self, bedroom, db):
        query = "INSERT INTO bedroom (type,price,capacity,description) VALUES (%s,%s,%s,%s)"
        values = (bedroom.type, bedroom.price, bedroom.capacity, bedroom.description)
        db.execute_query(query , values)
        print("Habitacion creada con exito")

    def all_bedrooms_repository(self,db):
        query ="SELECT * FROM bedroom where status=1"
        results = db.execute_query(query)
        return results

    def disable_bedroom_repository(self,bedroom,db):
        query = "UPDATE bedroom set status = 0 where id_bedroom = %s"
        values=(bedroom.id_bedroom,)
        db.execute_query(query,values)