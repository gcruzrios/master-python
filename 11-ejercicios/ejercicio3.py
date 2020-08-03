"""

ejercicio 3

Comprueba qie si una variable está vacia , rellenarla con texto en mayusculas y mostrarlo en minusculas

"""

texto =""

if len(texto.strip()) <= 0:

    texto ="Soy un texto en minusculas"
    print(texto.upper())

else:

    print(f"La variable tiene contenido {texto}")

    