class Alumno:
    def _init_(self, rut, nombre, direccion, correo, edad, nem):
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.correo = correo
        self.edad = edad
        self.nem = nem

def registrar_alumno():
    rut = int(input("Ingrese Rut del alumno (sin dígito verificador ni puntos): "))
    while rut < 500000 or rut > 39999999:
        rut = int(input("Rut fuera de rango. Ingrese Rut del alumno nuevamente: "))

    nombre = input("Ingrese Nombre del alumno: ")
    while nombre == "":
        nombre = input("Nombre no puede estar vacío. Ingrese Nombre del alumno nuevamente: ")

    direccion = input("Ingrese Dirección del alumno: ")
    while direccion == "":
        direccion = input("Dirección no puede estar vacía. Ingrese Dirección del alumno nuevamente: ")

    correo = input("Ingrese Correo electrónico del alumno: ")
    while "@" not in correo:
        correo = input("Correo electrónico inválido. Ingrese Correo electrónico del alumno nuevamente: ")

    edad = int(input("Ingrese Edad del alumno: "))
    while edad < 17 or edad > 90:
        edad = int(input("Edad fuera de rango. Ingrese Edad del alumno nuevamente: "))

    nem = float(input("Ingrese NEM del alumno: "))

    return Alumno(rut, nombre, direccion, correo, edad, nem)

def consultar_datos_alumno(alumnos, rut):
    for alumno in alumnos:
        if alumno.rut == rut:
            print("Datos del alumno:")
            print(f"Rut: {alumno.rut}")
            print(f"Nombre: {alumno.nombre}")
            print(f"Dirección: {alumno.direccion}")
            print(f"Correo electrónico: {alumno.correo}")
            print(f"Edad: {alumno.edad}")
            print(f"NEM: {alumno.nem}")
            if alumno.nem < 5.2:
                print("Alumno no cumple con requisitos")
            else:
                print("Alumno cumple con requisitos")
            return
    print("Alumno no encontrado")

def main():
    # Usuario y contraseña del administrador
    admin_user = "admin"
    admin_pass = "admin"

    # Base de datos de alumnos
    alumnos = []

    while True:
        print("\nSistema de Gestión de Alumnos")
        print("1) Registrar Alumno")
        if input("Ingrese usuario: ") == admin_user and input("Ingrese contraseña: ") == admin_pass:
            print("2) Consultar Datos de Alumno (Requiere permisos de administrador)")
        print("3) Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            alumno = registrar_alumno()
            alumnos.append(alumno)
            print("Alumno registrado exitosamente.")

        elif opcion == "2" and (input("Ingrese usuario: ") == admin_user and input("Ingrese contraseña: ") == admin_pass):
            rut_consulta = int(input("Ingrese Rut del alumno a consultar: "))
            consultar_datos_alumno(alumnos, rut_consulta)

        elif opcion == "3":
            print("Ha salido del sistema...")
            break

        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__=="main":
    main