
#Capturar errores
"""
try:
    nombre = input("Cual es tu nombre? : ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es "+ nombre

    print(nombre_usuario)
except:
    print("Error, el nombre es invalido")
else:
    print("Todo funciono bien")
finally:
    print("Fin del Script !!")


 # multiples excepciones   
try:
    numero = int(input ("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es : " + str(numero*numero))

except TypeError:
    print("Debe ser un número enteroS")

except ValueError:
    print("Debe ser un número no texto")

except Exception as e:
    print(type(e))
    print("Ha ocurrido un error ", type(e).__name__)    

"""

#Excepciones
try:
    nombre = input("Introduce el nombre")
    edad = int(input("Introduce la edad:"))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido al master en Python {nombre}  ")
except ValueError:
    print("Ingresa valores reales")
except Exception as e: 
       print("Ha ocurrido un error ", type(e).__name__)   