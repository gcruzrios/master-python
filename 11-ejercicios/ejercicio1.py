"""
Ejercicio 1

Hacer una lista de números enteros 

Recorrer la lista y mostrarla

Hacer una función que recorra listas de numeros
Ordenarla y mostrarla
Mostrar su longitud
Buscar un elemento (que el usuario pida por teclado)

"""

numeros=[13,64,52,73,21,7,91,63]
#1 lista

print("==============Recorrer y mostrar ==============")
for numero in numeros:
    print(numero)

#2 crear función

def mostrarLista(lista):
    resultado =""

    for elemento in numeros:
        resultado += "Elemento : " + str(elemento)
        resultado += "\n"

    return resultado

print(mostrarLista(numeros)) 

# Las funciones se definen antes de llamarlas

#3 ordenar y mostrar

print ("==========ordenar y mostrar ===========")

numeros.sort()
print(mostrarLista(numeros))

#4 Mostrar su longitud

print ("========== mostrar su longitud ===========")

#numeros.len() funcion de mostrar la longitud

print(len(numeros))


# busqueda en la lista

busqueda = int(input("Ingresa el valor: "))

comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
    busqueda = int(input("Ingresa el valor: "))
else:
    print(f"Has ingresado  el {busqueda}")

    
try:
    print(f"========== buscar en la lista el número {busqueda} =======")
    
    busqueda = int(input("Ingresa el valor: "))

    comprobar = isinstance(busqueda, int)

    while not comprobar or busqueda <= 0:
        busqueda = int(input("Ingresa el valor: "))
    else:
        print(f"Has ingresado  el {busqueda}")

    print(f"========== buscar en la lista el número {busqueda} =======")    
    
    search = numeros.index(busqueda)

    print(f"el número existe en la lista, es el indice : {search}" )
except:
    print ("Error, El número no está en la lista")    
