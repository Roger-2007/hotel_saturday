from domain.models.MandatoryService import MandatoryService

class MandatoryServiceRepository:
    def __init__(self):
        self.mandatory_service = MandatoryService

    def create_mandatory_service_repository(self , mandatory_service , db):
        query = "INSERT INTO mandatoryService (name,description,price) VALUES (%s,%s,%s)"
        values = mandatory_service.name , mandatory_service.description , mandatory_service.price
        db.execute_query(query,values)

    def all_mandatory_service_repository(self,db):
        query = "SELECT * FROM mandatoryService"
        result = db.execute_query(query)
        return result

    def update_mandatory_service_repository(self,mandatory_service,db):
        query = "UPDATE mandatoryService set name=%s,description=%s,price=%s where id=%s"
        values = (mandatory_service.name,mandatory_service.description,mandatory_service.price,mandatory_service.id)
        db.execute_query(query,values)

    def delete_mandatory_service_repository(self,mandatory_service,db):
        query = "DELETE from mandatoryService where id=%s"
        values = (mandatory_service.id,)
        db.execute_query(query,values)