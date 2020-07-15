
cantantes = ["2pack", "Drake", "Bad Bunny","Julio Iglesias"]
numeros = [1, 2, 5, 6, 8, 3, 61]

print(numeros)
numeros.sort()
print(numeros)

cantantes.append("Natos y waor")
cantantes.insert(1,"David Bisbal")

cantantes.pop(1)
cantantes.remove("Bad Bunny")

print(cantantes)

# dar la vuelta

numeros.reverse()
print(numeros)

#Buscar
print("Drake" in cantantes)

print(len(cantantes))

# cuantas veces aparece un elemento

numeros.append(18)
print(numeros.count(8))

# Conseguir indice
print(cantantes.index("Drake"))

cantantes.extend(numeros)
print(cantantes)