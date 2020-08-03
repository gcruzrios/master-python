"""

Escribir un programa que añada valores a una lista mientras su longitud sea menor a 120

usar while y for

"""

coleccion = []

for contador in range(0,120):
    coleccion.append(f"elemento-{contador}")
    print("Mostrando el: " + coleccion[contador])

print(coleccion[115])    

coleccion2 = []
x=0

while x < 120:
    coleccion2.append(f"elemento-{x}")
    print("Mostrando el: " + coleccion[x])
    x += 1

print(coleccion2[115])  