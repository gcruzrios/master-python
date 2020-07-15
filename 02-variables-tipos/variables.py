"""
Una variable es un contenedor de información
que dentro guardará un dato, se puede crear
muchas variables y que cada una tenga un dato distinto
"""
texto = "master en Python"
texto2= "Otra variable"

Numero=23
Decimal=0.7

print(texto)
print("texto2")
print(Numero)
print(Decimal)
print("-----------------------------------")
Numero=24
Decimal=1.7
print(Numero)
print(Decimal)
print("-----------------------------------")

#concatenar

Nombre ="Greivin"
Apellido="Cruz"
web ="www.greivin.net"

print(Nombre + " "+ Apellido + " - " + web)

print(f"{Nombre} {Apellido} - {web}")

print("Hola me llamo {} {} mi web es : {}".format(Nombre, Apellido, web))

print( Nombre, Apellido, web)