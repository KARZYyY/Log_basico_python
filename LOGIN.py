from colorama import init, Fore


init(autoreset=True)

def pedir_credenciales():
    nombre = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contrasena: ")
    return nombre, contrasena

def guardar_credenciales(nombre, contrasena, archivo="usuarios.txt"):
    with open(archivo, "a") as file:
        file.write("{} {}\n".format(nombre, contrasena))

def cargar_credenciales(archivo="usuarios.txt"):
    credenciales = []
    try:
        with open(archivo, "r") as file:
            for linea in file:
                nombre, contrasena = linea.strip().split()
                credenciales.append((nombre, contrasena))
    except FileNotFoundError:
        # Si no existe el archivo se crea uno para guardar las credenciales
        pass
    return credenciales

def registrar_usuario():
    print(Fore.GREEN + "¡Bienvenido al proceso de registro!")
    nombre, contrasena = pedir_credenciales()
    guardar_credenciales(nombre, contrasena)
    print(Fore.GREEN + "Registro exitoso. Puede iniciar sesión ahora.")

def validacion(nombre, contrasena, credenciales):
    # Esto valida si el nombre y la contraseña coinciden con las almacenadas
    for stored_nombre, stored_contrasena in credenciales:
        if nombre == stored_nombre and contrasena == stored_contrasena:
            return True
    return False

def iniciar_sesion():
    print(Fore.BLUE + "¡Bienvenido al sistema de inicio de sesión!")
    credenciales = cargar_credenciales()
    
    intentos_maximos = 3
    intentos = 0
    
    while intentos < intentos_maximos:
        nombre, contrasena = pedir_credenciales()
        
        if validacion(nombre, contrasena, credenciales):
            print(Fore.BLUE + "Inicio de sesión exitoso. ¡Bienvenido, {}!".format(nombre))
            break
        else:
            intentos += 1
            print(Fore.BLUE + "Credenciales incorrectas. Intento {}/{}".format(intentos, intentos_maximos))
    
    if intentos == intentos_maximos:
        print(Fore.RED + "Demasiados intentos incorrectos. Cerrando el programa.")


while True:
    
    print("\n" + Fore.GREEN + "Bienvenido al sistema de autenticación")
    print(Fore.GREEN + "1. Iniciar Sesión")
    print(Fore.BLUE + "2. Registrarse")
    print(Fore.RED + "3. Salir")

    opcion = input(Fore.RESET + "Seleccione una opción (1, 2 o 3): ")

    if opcion == "1":
        iniciar_sesion()
    elif opcion == "2":
        registrar_usuario()
    elif opcion == "3":
        print(Fore.RED + "Cerrando el programa. ¡Hasta luego!")
        break
    else:
        print(Fore.RED + "Opción no válida. Inténtelo de nuevo.")

                                                          #PROJECT BY KARZY