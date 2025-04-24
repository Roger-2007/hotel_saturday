



from domain.models.Guest import Guest
from application.GuestService import GuestService
from application.GuestInput import GuestInput
from repository.conexion.Conexion import Conexion
from application.BedroomInput import BedroomInput
from domain.models.Bedroom import Bedroom
from application.MandatoryServiceInput import MandatoryServiceInput
from application.OptionalServiceInput import OptionalServiceInput



class Menu_App:

    db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel_saturday')
    db.connection()

    def __init__(self):
        self.guest = Guest(None, None,None,None,None,None,None,None,None)
        self.bedroom = Bedroom(None,None,None,None,None,None)
        self.guest_service = GuestService()
        self.guest_input = GuestInput()
        self.bedroom_input = BedroomInput()
        self.mandatory_service_input = MandatoryServiceInput()
        self.optional_service_input = OptionalServiceInput()


    def init_app(self):
        init = (int(input("Presione 1 para inicializar")))

        while init != 0:

            option = int(input("1. Login 2. registro 3. salir"))

            match option:
                case 1: #LOGIN
                    select = 0
                    select = int(input("Quien se quiere loguear\n1.Huesped\n2.Empleado"))
                    match select:
                        case 1: #LOGIN - GUEST
                            datos = self.guest_input.login(self.db)
                            if not datos:
                                print("Huesped no encontrado")
                            else:
                                id_guest = datos[0][0]
                                option_login=0
                                while option_login != 4:
                                    option_login = int(input("\n1. Hacer una reservacion\n2. Editar perfil\n3. Borrar perfil\n4. Cerrar sesion"))

                                    match option_login:
                                        #case 1:



                                        case 2: #UPDATE - GUEST
                                            self.guest_input.update(id_guest,self.db)
                                            option_login=4
                                        case 3: #DISABLE GUEST
                                            self.guest_input.disable(id_guest,self.db)
                                            option_login=4
                                        case _: #INCORRECT OPTION
                                            print("Opcion invalida")


                case 2 : #REGISTER
                    print("Registro")
                    self.guest_input.register(self.guest,self.db)

                case 3: #FINISH
                    print("Finalizaste con exito")
                    init=0

                case _: #INCORRECT OPTION
                    print("Opcion invalida")





