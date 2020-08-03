import getpass
import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("Ok, vamos a registrar tu usuario en el sistema...")

        nombre = input("Cual es tu nombre?: ")
        apellidos = input("Cuales son tus apellidos?: ")
        email = input("Ingresa tu email: ")
        #password = input("Introduce tu contraseña: ")
        password = getpass.getpass("Ingresa la contraseña: ")
        #print(password)

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto, {registro[1].nombre} ha sido registrado con el email {registro[1].email}")
        else:
            print("No se realizó el registro...")    

    def login(self):
        print("Ingresar al sistema...")
        try:
            email = input("Email: ")
            #password = input("Introduce tu contraseña: ")
            password = getpass.getpass("Contraseña: ")  

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()  

            if email == login[3]:
                print(f"\n Bienvenido {login[1]}, te has registrado previamente...")
                self.proximasAcciones(login)
        
        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Login incorrecto, intentar más tarde")



    def proximasAcciones(self, usuario):
        print("""
        
        Acciones disponibles

            1. Crear Notas
            2. Mostrar tus notas
            3. Eliminar tus notas
            4. Salir

            """)

        accion = input("Digite el Nº de opción: ")

        Doit = notas.acciones.Acciones()

        if accion == "1":
            print("Vamos a crear")
            Doit.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "2":
            print("Vamos a mostrar")
            Doit.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "3":
            print("Vamos a eliminar")
            Doit.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "4":
            print(f"Hasta Luego, {usuario[1]}")
            exit()
            
        return None   

