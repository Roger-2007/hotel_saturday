
from domain.models.Guest import  Guest
#from repository.persistence.GuestRepository import GuestRepository
from domain.service.GuestService import GuestService
import re

class GuestInput:


    def __init__(self):
        self.guest = Guest(None,None,None,None ,None,None, None,None,None )
        self.guest_service = GuestService()


    def register(self, db):

        while True:
             try:
                id_guest = int(input("\nIngrese su documento de identidad"))
                texto = str(id_guest)
                es_valido = re.fullmatch(r"\d{7,12}$",texto)
                if es_valido:
                    self.guest.id_guest = id_guest
                    break
                else:
                    print("\nEl ID debe tener entre 7 y 12 numeros\n")
             except ValueError:
                 print("\nEl ID solo puede ser numeros\n")
             except Exception as e:
                 print(f"\nOcurrió un error al ingresar el id: {e}")
        while True:
            try:
                name = input("Ingrese su nombre")
                es_valido = re.fullmatch(r"^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$",name)
                if es_valido:
                    self.guest.name = name
                    break
                else:
                    print("\nSolo se permiten letras\n")
            except Exception as e:
                print(f"\nOcurrió un error: {e}\n")
        while True:
            try:
                last_name = input("Ingrese su apellido")
                es_valido = re.fullmatch(r"^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", last_name)
                if es_valido:
                    self.guest.last_name = last_name
                    break
                else:
                    print("\nSolo se permiten letras\n")

            except Exception as e:
                print(f"\nOcurrió un error: {e}\n")

        while True:
             try:
                phone = input("Ingrese su teléfono")
                es_valido = re.fullmatch(r"\d{7,10}$",phone)
                if es_valido:
                    self.guest.phone = phone
                    break
                else:
                    print("\nEl numero de telefono debe tener entre 7 y 10 digitos\n")
             except ValueError:
                 print("\nEl numero de telefono solo puede ser numeros\n")
             except Exception as e:
                 print(f"\nOcurrió un error al ingresar el numero de telefono: {e}")


        while True:
             try:
                email = input("Ingrese su correo")
                es_valido = re.fullmatch(r"^[a-zA-Z0-9._-]{6,30}@(gmail|hotmail|outlook)\.[a-zA-Z]{2,5}$",email)
                if es_valido:
                    self.guest.email = email
                    break
                else:
                    print("\nEl correo debe tener entre 6 a 30 letras, números o algunos símbolos antes del @, seguido de un dominio valido y al menos un punto antes de la extensión.\nejemplo@gmail.com\n")
             except Exception as e:
                 print(f"\nOcurrió un error{e}\n")

        while True:
            try:
                password = input("Ingrese su contraseña")
                es_valido = re.fullmatch(r"^[a-zA-Z0-9._-]{6,20}$",password)
                if es_valido:
                    self.guest.password = password
                    break
                else:
                    print("\nLa contraseña debe contener entre 6 a 20 letras, numeros, puntos, guiones o guiones bajos\n")
            except Exception as e:
                print(f"Ocurrió un error{e}")

        while True:
            try:
                origin = input("Ingrese su ciudad de origen")
                es_valido = re.fullmatch(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",origin)
                if es_valido:
                    self.guest.origin = origin
                    break
                else:
                    print(f"El origen solo puede contener letras")
            except Exception as e:
                print(f"Ocurró un error{e}")

        while True:
            try:
                occupation = input("Ingrese su ocupacion")
                es_valido = re.fullmatch(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",occupation)
                if es_valido:
                    self.guest.occupation = occupation
                    break
                else:
                    print("La ocupacion solo puede contener letras")
            except Exception as e:
                print(f"Ocurrio un error{e}")


        self.guest_service.create_guest_service(self.guest, db)


    def login(self,db):
        while True:
            try:
                email = input("Ingrese su correo")
                es_valido = re.fullmatch(r"^[a-zA-Z0-9._-]{6,30}@(gmail|hotmail|outlook)\.[a-zA-Z]{2,5}$", email)
                if es_valido:
                    self.guest.email = email
                    break
                else:
                    print(
                        "\nEl correo debe tener entre 6 a 30 letras, números o algunos símbolos antes del @, seguido de un dominio valido y al menos un punto antes de la extensión.\nejemplo@gmail.com\n")
            except Exception as e:
                print(f"\nOcurrió un error{e}\n")

        while True:
            try:
                password = input("Ingrese su contraseña")
                es_valido = re.fullmatch(r"^[a-zA-Z0-9._-]{6,20}$", password)
                if es_valido:
                    self.guest.password = password
                    break
                else:
                    print(
                        "\nLa contraseña debe contener entre 6 a 20 letras, numeros, puntos, guiones o guiones bajos\n")
            except Exception as e:
                print(f"Ocurrió un error{e}")
        return self.guest_service.login_guest_service(self.guest,db)

    def update(self,id_guest,db):
        self.guest.id_guest = id_guest
        while True:
            try:
                name = input("Ingrese su nombre")
                es_valido = re.fullmatch(r"^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", name)
                if es_valido:
                    self.guest.name = name
                    break
                else:
                    print("\nSolo se permiten letras\n")
            except Exception as e:
                print(f"\nOcurrió un error: {e}\n")
        while True:
            try:
                last_name = input("Ingrese su apellido")
                es_valido = re.fullmatch(r"^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", last_name)
                if es_valido:
                    self.guest.last_name = last_name
                    break
                else:
                    print("\nSolo se permiten letras\n")

            except Exception as e:
                print(f"\nOcurrió un error: {e}\n")

        while True:
            try:
                phone = input("Ingrese su teléfono")
                es_valido = re.fullmatch(r"\d{7,10}$", phone)
                if es_valido:
                    self.guest.phone = phone
                    break
                else:
                    print("\nEl numero de telefono debe tener entre 7 y 10 digitos\n")
            except ValueError:
                print("\nEl numero de telefono solo puede ser numeros\n")
            except Exception as e:
                print(f"\nOcurrió un error al ingresar el numero de telefono: {e}")

        while True:
            try:
                email = input("Ingrese su correo")
                es_valido = re.fullmatch(r"^[a-zA-Z0-9._-]{6,30}@(gmail|hotmail|outlook)\.[a-zA-Z]{2,5}$", email)
                if es_valido:
                    self.guest.email = email
                    break
                else:
                    print(
                        "\nEl correo debe tener entre 6 a 30 letras, números o algunos símbolos antes del @, seguido de un dominio valido y al menos un punto antes de la extensión.\nejemplo@gmail.com\n")
            except Exception as e:
                print(f"\nOcurrió un error{e}\n")

        while True:
            try:
                password = input("Ingrese su contraseña")
                es_valido = re.fullmatch(r"^[a-zA-Z0-9._-]{6,20}$", password)
                if es_valido:
                    self.guest.password = password
                    break
                else:
                    print(
                        "\nLa contraseña debe contener entre 6 a 20 letras, numeros, puntos, guiones o guiones bajos\n")
            except Exception as e:
                print(f"Ocurrió un error{e}")

        while True:
            try:
                origin = input("Ingrese su ciudad de origen")
                es_valido = re.fullmatch(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", origin)
                if es_valido:
                    self.guest.origin = origin
                    break
                else:
                    print(f"El origen solo puede contener letras")
            except Exception as e:
                print(f"Ocurró un error{e}")

        while True:
            try:
                occupation = input("Ingrese su ocupacion")
                es_valido = re.fullmatch(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", occupation)
                if es_valido:
                    self.guest.occupation = occupation
                    break
                else:
                    print("La ocupacion solo puede contener letras")
            except Exception as e:
                print(f"Ocurrio un error{e}")
        self.guest_service.update_guest_service(self.guest, db)

    def disable(self,id_guest,db):
        self.guest.id_guest=id_guest
        self.guest_service.disable_guest_service(self.guest,db)

    def delete(self,id_guest,db):
        self.guest.id_guest=id_guest
        self.guest_service.delete_guest_service(self.guest,db)








