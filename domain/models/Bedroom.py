class Bedroom:
    def __init__(self,id_bedroom,type,price,capacity,description,status):
        self._id_bedroom=id_bedroom
        self._type=type
        self._price=price
        self._capacity=capacity
        self._description=description
        self._status=status

    @property
    def id_bedroom(self):
        return self._id_bedroom

    @id_bedroom.setter
    def id_bedroom(self,id_bedroom):
        self._id_bedroom=id_bedroom

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self,type):
        self._type=type

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,price):
        self._price=price

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        self._capacity=capacity

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self,description):
        self._description=description

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,status):
        self._status=status


