nombre ="Greivin Cruz"

print(nombre)
print(type(nombre))

comprobar = isinstance(nombre, str)

if comprobar :
    print("Esa variable es un string")
else:
    print("No es string")

if not isinstance(nombre, float):

    print ("la variable no es numero flotante")

frase = "    mi contenido    " 

print(frase)
print(frase.strip())


year=2021
del year
#print(year)

texto = "  ff  "

if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido ", len (texto))    

# encontrar caracteres

frase = "La vida es bella"

print(frase.find("vida"))

nueva_frase = frase.replace("vida", "moto")
print (nueva_frase)

print(nombre)
print(nombre.lower())
print(nombre.upper())