from domain.models.Employee import Employee
from repository.persistence.EmployeeRepository import EmployeeRepository

class EmployeeInput:
    def __init__(self):
        self.employee=Employee(None,None,None,None,None,None,None,None)
        self.employee_repository=EmployeeRepository()

    def create_employee(self,db):
        id = int(input("Ingrese su documento de identidad"))
        self.employee.id = id
        name = input("Ingrese su nombre")
        self.employee.name = name
        last_name = input("Ingrese su apellido")
        self.employee.last_name = last_name
        phone = input("Ingrese su teléfono")
        self.employee.phone = phone
        email = input("Ingrese su correo")
        self.employee.email = email
        password = input("Ingrese su contraseña")
        self.employee.password = password
        rol = input("Ingrese su rol")
        self.employee.rol = rol
        self.employee_repository.create_employee_repository(self.employee,db)

    def login_employee(self,db):
        self.employee.email = input("Ingrese su email")
        self.employee.password = input("Ingrese su contraseña")
        return self.employee_repository.login_employee_repository(self.employee, db)
