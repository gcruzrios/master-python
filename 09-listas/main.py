"""
Listas (array)

Son colecciones o conjuntos de datos valores bajo un único nombre
para acceder a esos valores podemos usar indice numerico


"""

pelicula = "Batman"

#definir la lista
peliculas = ["Batman", "SpiderMan", "El señor de los anillos"]

cantantes = list(("2pack", "drake", "Jennifer Lopez"))

years = list(range(2020, 2050))

variada = ["Greivin", 30, True, "Cruz"]

"""
print (peliculas)
print (cantantes)
print (years)
print (variada)
"""

#Indices

pelicula = "Otra cosa"
peliculas[1] ="Gran Torino"
peliculas[2] ="El hobbit"
print(peliculas[1])
print(cantantes[1:3])
print(cantantes[0:1])
print(peliculas[1:3])

# Añadir elementos a la lista

cantantes.append("Kase O")
cantantes.append("Natos y waor")
print(cantantes)

# Recorrer lista

print("\n==================LISTADO de PELICULAS ==================")

nueva_pelicula ="parar"

while nueva_pelicula !="parar": 
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1} {pelicula}")


# Listas multidimensionales

print("\n==================LISTADO de CONTACTOS ==================")

contactos = [
    [
        'Antonio',
        'antonio@correo.com'
    ],
    [
        'Luis',
        'luis@correo.com'
    ],
    [
        'Ana',
        'ana@correo.com'
    ],
    
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: "+ elemento)
        else:
            print("Email: " + elemento)
print("\n")

# print(contacto[0])
#print(contactos[1][1])