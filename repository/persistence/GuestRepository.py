import mysql.connector

from domain.models.Guest import Guest



class GuestRepository:


    def __init__(self):
        self.guest = Guest


    def create_guest_repository(self, guest, db):
       # try:
            query = "INSERT INTO guest (id_guest,name,last_name,phone,email,password,origin,occupation) VALUES (%s,%s,%s, %s, %s, %s,%s, %s)"
            values = (guest.id_guest, guest.name, guest.last_name , guest.phone, guest.email , guest.password  , guest.origin , guest.occupation)
            db.execute_query(query , values)
       # except (mysql.connector.IntegrityError,Exception) as e:
        #   raise Exception(e)


    def login_guest_repository(self,guest,db):
        query = "SELECT * FROM guest where email=%s and password=%s and status=1"
        values = (guest.email,guest.password)
        result = db.execute_query(query,values)
        return result

    def update_guest_repository(self,guest,db):
        query = "update guest set name=%s,last_name=%s,phone=%s,email=%s,password=%s,origin=%s,occupation=%s where id_guest=%s and status=1"
        values = (guest.name,guest.last_name,guest.phone,guest.email,guest.password,guest.origin,guest.occupation,guest.id_guest)
        db.execute_query(query,values)

    def all_guest_repository(self,db):
        query = "SELECT * FROM guest"
        results = db.execute_query(query)
        return results

    def disable_guest_repository(self,guest,db):
        query = "UPDATE guest set status=0 where id_guest=%s"
        values = (guest.id_guest,)
        db.execute_query(query,values)

    def delete_guest_repository(self,guest,db):
        query = "delete from guest where id_guest=%s"
        values = (guest.id_guest,)
        db.execute_query(query,values)