"""
FUNCIONES

conjunto de instrucciones agrupadas bajo nombre concreto que pueden reutilizarse invocando tantas veces como sea
necesario.

def nombredeMiFuncion(parametros)

    #bloque de /contenido de instrucciones


"""

#Ejemplo(1)

print("==================EJEMPLO 1 ====================")

def muestraNombre():
    print("Greivin")
    print("Juan")
    print("Francisco")
    print("Victor")
    print("Nestor")
    print("\n")

# Invocar funcion

muestraNombre()
"""
print("==================EJEMPLO 2 ====================")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

def mostrarTuNombre(nombre, edad):
        print(f"Tu Nombre es : {nombre}")

        if edad >= 18:

            print("Eres mayor de edad")


mostrarTuNombre("Greivin Cruz")
mostrarTuNombre("Paquito")
mostrarTuNombre("Juan Fran")
mostrarTuNombre(nombre,edad)
"""


print("==================EJEMPLO 3 ====================")

def tabla(numero):

    print(f"tabla de multiplicar del número : {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")

tabla(3)
tabla(7)    

print("==================EJEMPLO 3.1 ====================")

for numero_tabla in range(1,11):
    tabla(numero_tabla)

print("==================EJEMPLO 4 ====================")
#parametros opcionales

def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    #print(f"DNI: {dni}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Greivin Cruz", "1872394")

print("==================EJEMPLO 5 ====================")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

print(saludame("Greivin Cruz"))


print("==================EJEMPLO 6 ====================")

def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2
    cadena = ""
    if basicas != False:
        
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n" 
    else:
        cadena += "Multi: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)
        cadena += "\n"

    return cadena


print(calculadora( 56,5, True))

print("\n==================EJEMPLO 7 ====================")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

#print(getNombre("Victor"), getApellido("Robles"))
print(devuelveTodo("Victor", "Robles"))

print("\n==================EJEMPLO 8 ====================")

dime_el_year = lambda year: f"El año es { year * 50 } "

print(dime_el_year(2034))