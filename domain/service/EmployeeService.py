from repository.persistence.EmployeeRepository import EmployeeRepository
class EmployeeService:
    def __init__(self):
        self.employee_repository = EmployeeRepository()

    def create_employee_service(self,employee,db):
        try:
            self.employee_repository.create_employee_repository(employee,db)
            print("\nSe creo el empleado correctamente\n")
        except Exception as e:
            print(f"\nOcurrió un error al crear el empelado: {e}\n")

    def login_employee_service(self,employee,db):
        try:
            resultado = self.employee_repository.login_employee_repository(employee,db)
            if resultado:
                print("\nInicio de sesion exitoso\n")
                return resultado
            else:
                print("\nCorreo o contraseña incorrectos\n")
                return resultado
        except Exception as e:
            print(f"Ocurrió un error al loguear al empleado: {e}")
