"""
Modulos

son funcionalidades ya hechas para reutilizar

En python hay muchos módulos

https://docs.python.org/3/library

Podemos conseguir modulos en el lenguaje,  Internet

O desarrollados por nosotros
"""

# Importar modulo propio

import mimodulo
from mimodulo import *
from mimodulo import holamundo

#print (mimodulo.holamundo("Greivin Cruz, web"))

print (holamundo("Greivin Cruz, web"))

print (mimodulo.calculadora(3,5, True))

#modulos datetime

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)

print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S" )
print("Mi fecha personalizada", fecha_personalizada)

import math

print("raiz cuadrada de 10: ", math.sqrt(10))

print ("Numero Pi: " , float(math.pi))


import random

print("Numero aleatorio entre 15 y 67 :", random.randint(15,67))
