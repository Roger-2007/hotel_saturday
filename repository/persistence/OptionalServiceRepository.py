from domain.models.OptionalService import OptionalService

class OptionalServiceRepository:
    def __init__(self):
        self.optional_service = OptionalService

    def create_optional_service(self , optional_service , db):
        query = "INSERT INTO optionalService (id,name,description,price) VALUES (%s,%s,%s,%s)"
        values = optional_service.id , optional_service.name , optional_service.description , optional_service.price
        db.execute_query(query,values)
        