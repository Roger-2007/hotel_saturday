from domain.models.Service import Service

class OptionalService(Service):
    def __init__(self,id,name,description,price):
        super().__init__(id,name,description,price)