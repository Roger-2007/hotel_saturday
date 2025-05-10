import mysql.connector

from domain.models.Guest import Guest
from repository.persistence.GuestRepository import GuestRepository


class GuestService:

    def __init__(self):
        self.guest = Guest(None, None, None, None, None, None, None, None, None)
        self.guest_repository = GuestRepository()

    def create_guest_service(self, guest, db):
        try:
            self.guest_repository.create_guest_repository(guest, db)
            print("\nSe registro el huesped correctamente!\n")

        except mysql.connector.IntegrityError:
            print( f"\nNo se pudo crear huesped:\nYa existe un huesped con el ID: {guest.id_guest}\n")

        except Exception as e:
            print(f"\nOcurrió un error al crear el huesped: {e}\n")


    def login_guest_service(self,guest,db):
        try:
            guest_login = self.guest_repository.login_guest_repository(guest,db)
            if not guest_login:
                print("\nCorreo o contraseña incorrectos\n")
            else:
                print("\nInicio de sesion exitoso\n")
            return guest_login
        except Exception as e:
            print(f"\nOcurrió un error al iniciar sesion: {e}\n")

    def update_guest_service(self,guest,db):
        try:
            self.guest_repository.update_guest_repository(guest,db)
            print("\nSe actualizo el huesped correctamente\n")
        except Exception as e:
            print(f"\nOcurrió un error al actualizar el huesped: {e}\n")

    def disable_guest_service(self,guest,db):
        try:
            self.guest_repository.disable_guest_repository(guest,db)
            print(f"\nSe deshabilitó correctamente el huesped con id: {guest.id_guest}\n")
        except Exception as e:
            print(f"\nOcurrio un error al deshabilitar el huesped: {e}\n")

    def delete_guest_service(self,guest,db):
        try:
            self.guest_repository.delete_guest_repository(guest,db)
            print(f"\nSe elimino correctamente el huesped con id: {guest.id_guest}\n")
        except Exception as e:
            print(f"\nOcurrio un error al eliminar el huesped: {e}\n")