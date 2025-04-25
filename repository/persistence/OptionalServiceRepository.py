from domain.models.OptionalService import OptionalService

class OptionalServiceRepository:
    def __init__(self):
        self.optional_service = OptionalService

    def create_optional_service_repository(self , optional_service , db):
        query = "INSERT INTO optionalservice (name,description,price) VALUES (%s,%s,%s)"
        values = optional_service.name , optional_service.description , optional_service.price
        db.execute_query(query,values)
        print("Servicio creado con exito")

    def all_optional_service_repository(self,db):
        query = "SELECT * FROM optionalservice"
        result = db.execute_query(query)
        return result

    def update_optional_service_repository(self,optional_service,db):
        query = "UPDATE optionalservice set name=%s,description=%s,price=%s where id=%s"
        values = (optional_service.name,optional_service.description,optional_service.price,optional_service.id)
        db.execute_query(query,values)

    def delete_optional_service_repository(self,optional_service,db):
        query = "DELETE from optionalservice where id=%s"
        values = (optional_service.id,)
        db.execute_query(query,values)

