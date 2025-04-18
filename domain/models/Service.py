class Service:
    def __init__(self,id,name,description,price):
        self._id=id
        self._name=name
        self._description=description
        self._price=price

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        self._id=id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self,description):
        self._description=description

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,price):
        self._price=price

