from domain.models.Employee import Employee
from domain.service.EmployeeService import EmployeeService
import re

class EmployeeInput:
    def __init__(self):
        self.employee=Employee(None,None,None,None,None,None,None,None)
        self.employee_service=EmployeeService()

    def create_employee(self,db):
        while True:
             try:
                id= int(input("\nIngrese su documento de identidad"))
                texto = str(id)
                es_valido = re.fullmatch(r"\d{7,12}$",texto)
                if es_valido:
                    self.employee.id = id
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
                    self.employee.name = name
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
                    self.employee.last_name = last_name
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
                    self.employee.phone = phone
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
                    self.employee.email = email
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
                    self.employee.password = password
                    break
                else:
                    print("\nLa contraseña debe contener entre 6 a 20 letras, numeros, puntos, guiones o guiones bajos\n")
            except Exception as e:
                print(f"Ocurrió un error{e}")

        while True:
            try:
                rol = input("Ingrese su rol")
                es_valido = re.fullmatch(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",rol)
                if es_valido:
                    self.employee.rol = rol
                    break
                else:
                    print(f"El rol solo puede contener letras")
            except Exception as e:
                print(f"Ocurró un error{e}")

        self.employee_service.create_employee_service(self.employee,db)

    def login_employee(self,db):
        self.employee.email = input("Ingrese su email")
        self.employee.password = input("Ingrese su contraseña")
        return self.employee_service.login_employee_service(self.employee, db)
