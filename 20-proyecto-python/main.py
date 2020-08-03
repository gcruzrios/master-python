"""

Proyecto Python y MySQL

Abrir asistente
Login o registro


Si eligimos registro, creara un usuario en la bd
Si eligimos login , identifica al usuario y nos pregunta
Crear nota, mostrar notas, borrarlas.

"""
from usuarios import acciones
print ("""

Acciones disponibles:

1. Hacer un registro
2. Login al sistema



""")
Doit = acciones.Acciones()
accion = input ("Digitar Número de opción :")

if accion == "1":

    Doit.registro()

elif accion == "2":
    Doit.login()