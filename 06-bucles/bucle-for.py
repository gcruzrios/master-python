"""
# FOR

for variable in elemento iterable (lista, rango, etc)

Bloque de instrucciones

"""

contador = 0
resultado = 0
for contador in range(0,10):

    print ("¡voy por el " + str(contador))

    #resultado = resultado + contador
    resultado += contador

    print(f"EL resultado es {resultado}")


print ( "\n ==================== EJEMPLO =====================")


numero_usuario = int(input("de que número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f" ==== Tabla de multiplicar del número {numero_usuario} =========")    

for numero_tabla in range(1,11):

    if numero_usuario == 45:
        print("No se pueden mostrar numeros prohibidos")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")

else:
    print("Tabla Finalizada")    