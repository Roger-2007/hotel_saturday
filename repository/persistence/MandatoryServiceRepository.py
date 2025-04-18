from domain.models.MandatoryService import MandatoryService

class MandatoryServiceRepository:
    def __init__(self):
        self.mandatory_service = MandatoryService

    def create_mandatory_service(self , mandatory_service , db):
        query = "INSERT INTO mandatoryService (id,name,description,price) VALUES (%s,%s,%s,%s)"
        values = mandatory_service.id , mandatory_service.name , mandatory_service.description , mandatory_service.price
        db.execute_query(query,values)
        