"""
SET es un tipo de dato de colección de valores
pero no tienen indice, ni orden

"""

personas = {
    "Victor", 
    "Manolo",
    "Francisco"
}

personas.add("Paco")

personas.remove("Francisco")


print(type(personas))
print(personas)