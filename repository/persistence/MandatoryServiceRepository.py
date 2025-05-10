from domain.models.MandatoryService import MandatoryService

class MandatoryServiceRepository:
    def __init__(self):
        self.mandatory_service = MandatoryService

    def create_mandatory_service_repository(self , mandatory_service , db):
        query = "INSERT INTO mandatoryservice (name,description,price) VALUES (%s,%s,%s)"
        values = mandatory_service.name , mandatory_service.description , mandatory_service.price
        db.execute_query(query,values)

    def all_mandatory_service_repository(self,db):
        query = "SELECT * FROM mandatoryservice"
        result = db.execute_query(query)
        return result

    def update_mandatory_service_repository(self,mandatory_service,db):
        query = "UPDATE mandatoryservice set name=%s,description=%s,price=%s where id=%s"
        values = (mandatory_service.name,mandatory_service.description,mandatory_service.price,mandatory_service.id)
        db.execute_query(query,values)

    def delete_mandatory_service_repository(self,mandatory_service,db):
        query = "DELETE from mandatoryservice where id=%s"
        values = (mandatory_service.id,)
        db.execute_query(query,values)

    def get_total_price_mandatory_service_repository(self,db):
        query = "SELECT sum(price) from mandatoryservice"
        result = db.execute_query(query)
        return result