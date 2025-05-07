from domain.models.Guest import Guest
from domain.service.GuestService import GuestService
from application.GuestInput import GuestInput
from repository.conexion.Conexion import Conexion
from application.BedroomInput import BedroomInput
from domain.models.Bedroom import Bedroom
from application.MandatoryServiceInput import MandatoryServiceInput
from application.OptionalServiceInput import OptionalServiceInput
from application.BookingInput import BookingInput
from application.Reservacion_ServicioOpcionalInput import Reservacion_ServicioOpcionalInput
from application.EmployeeInput import EmployeeInput


class Menu_App:
    db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel_saturday')
    db.connection()

    def __init__(self):
        self.guest = Guest(None, None, None, None, None, None, None, None, None)
        self.bedroom = Bedroom(None, None, None, None, None, None)
        self.guest_service = GuestService()
        self.guest_input = GuestInput()
        self.bedroom_input = BedroomInput()
        self.mandatory_service_input = MandatoryServiceInput()
        self.optional_service_input = OptionalServiceInput()
        self.booking_input = BookingInput()
        self.booking_optional_service_input = Reservacion_ServicioOpcionalInput()
        self.employee_input = EmployeeInput()

    def select_bedroom(self, all_bedrooms):
            print("")
            for i, bedroom in enumerate(all_bedrooms):
                print(
                    f"{i + 1}. Tipo de habitación: {bedroom[1]} - precio: {bedroom[2]} - capacidad para {bedroom[3]} personas")
            while True:
                try:
                    option = int(input("Seleccione alguna habitación: "))
                    if 1 <= option <= len(all_bedrooms):
                        return all_bedrooms[option - 1]
                    else:
                        print("\nOpción invalida\n")
                except ValueError:
                    print("\nSolo se permiten numeros\n")

    def select_optional_services(self, optional_services, id_booking):
        while True:
            print("\nServicios opcionales disponibles:")
            for i, opt in enumerate(optional_services):
                print(f"{i + 1}. {opt[1]}, {opt[2]} - valor: {opt[3]}")
            try:
                option = int(input("Selecciona un servicio opcional o pulsa '0' para omitir: "))
                if option == 0:
                    break
                elif 1 <= option <= len(optional_services):
                    id_optional_service = optional_services[option - 1][0]
                    self.booking_optional_service_input.create_reservacion_servicio_opcional(
                        id_booking, id_optional_service, self.db)
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Entrada inválida.")



    def init_app(self):

        init = (int(input("Presione 1 para inicializar\n")))

        while init != 0:

            option = int(input("1. Login 2. registro 3. salir"))

            match option:
                case 1:  # LOGIN
                    select = 0
                    select = int(input("\nQuien se quiere loguear\n1.Huesped\n2.Empleado"))
                    match select:
                        case 1:  # LOGIN - GUEST
                            datos = self.guest_input.login(self.db)
                            if datos:

                                id_guest = datos[0][0]
                                option_login = 0
                                while option_login != 4:
                                    option_login = int(input(
                                        "1. Hacer una reservacion\n2. Editar perfil\n3. Borrar perfil\n4. Cerrar sesion"))

                                    match option_login:
                                        case 1:
                                            mandatory_service_total = 0
                                            optional_service_total = 0
                                            total = 0
                                            bedroom_price = 0
                                            days = 0
                                            mandatory_service = self.mandatory_service_input.all_mandatory_service(
                                                self.db)
                                            optional_service = self.optional_service_input.all_optional_service(self.db)
                                            all_bedrooms = self.bedroom_input.all_bedrooms(self.db)
                                            if not all_bedrooms:
                                                break
                                            option_bedroom = self.select_bedroom(all_bedrooms)
                                            id_bedroom = all_bedrooms[0]
                                            bedroom_price = all_bedrooms[2]
                                            mandatory_service_total = self.mandatory_service_input.get_total_price_mandatory_service(self.db)
                                            self.booking_input.create_booking(id_guest, id_bedroom, self.db)
                                            id_booking = self.booking_input.get_id_booking(id_guest, id_bedroom,self.db)

                                            option_optional = 1
                                            while option_optional != 0:

                                                for i, optservice in enumerate(optional_service):
                                                    print(
                                                        f"{i + 1}. {optservice[1]} , {optservice[2]} - valor: {optservice[3]}")
                                                option_optional = int(
                                                    input(
                                                        "Selecciona algun servicio opcional o pulsa '0' para omitir\n"))
                                                if option_optional != 0:
                                                    id_optional_service = optional_service[(option_optional - 1)][0]
                                                    self.booking_optional_service_input.create_reservacion_servicio_opcional(
                                                        id_booking[0][0], id_optional_service, self.db)
                                            optional_service_total = self.booking_input.get_total_price_optional_service(
                                                id_booking[0][0], self.db)
                                            days = self.booking_input.get_days(id_booking[0][0], self.db)
                                            self.bedroom_input.disable_bedroom(id_bedroom, self.db)
                                            #print(f"{mandatory_service_total[0][0]} {optional_service_total[0][0]} {bedroom_price} {days[0][0]}")
                                            total = mandatory_service_total[0][0] + optional_service_total[0][0] + (
                                                        bedroom_price * days[0][0])

                                            self.booking_input.update_total_booking(id_booking[0][0], total, self.db)
                                            option_login=4
                                        case 2:  # UPDATE - GUEST
                                            self.guest_input.update(id_guest, self.db)
                                            option_login = 4
                                        case 3:  # DISABLE GUEST
                                            self.guest_input.disable(id_guest, self.db)
                                            option_login = 4
                                        case 4:
                                            print("")
                                        case _:  # INCORRECT OPTION
                                            print("Opcion invalida")
                        case 2:
                            datos = self.employee_input.login_employee(self.db)
                            if not datos:
                                print("Empleado no encontrado")
                            else:
                                print("Sesion iniciada con exito!")
                                id = datos[0][0]
                                option_employee = 0
                                while option_employee!=4:
                                    option_employee=int(input("1. Habitacion\n2. Crear servicio obligatorio\n3. Crear servicio opcional\n4. Salir"))
                                    match option_employee:
                                        case 1:
                                            option_bedroom = int(input("1. Crear habitacion\n2. Ver todas las habitaciones"))
                                            match option_bedroom:
                                                case 1:
                                                    self.bedroom_input.create_bedroom(self.db)
                                                case 2:
                                                    all_bedrooms = self.bedroom_input.all_bedrooms(self.db)
                                                    for i, bedroom in enumerate(all_bedrooms):
                                                        print(f"{i + 1}. Tipo de habitacion: {bedroom[1]} - precio: {bedroom[2]} - capacidad para {bedroom[3]} personas")
                                        case 2:
                                            #option_mandatory = int(input("1.Crear servicio obligatorio\n"))
                                            self.mandatory_service_input.create_mandatory_service(self.db)
                                        case 3:
                                            self.optional_service_input.create_optional_service(self.db)
                                        case _:
                                            print("Opcion invalida")

                case 2:  # REGISTER

                    option_register = int(input("Quien se desea registrar?\n1. Huesped\n2. Empleado"))
                    match option_register:
                        case 1:
                            self.guest_input.register(self.guest, self.db)
                        case 2:
                            self.employee_input.create_employee(self.db)


                case 3:  # FINISH
                    print("Finalizaste con exito")
                    init = 0

                case _:  # INCORRECT OPTION
                    print("Opcion invalida")
