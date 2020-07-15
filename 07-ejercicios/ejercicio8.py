# porcentaje de un número

numero = int(input("introduce el un número: "))
porcentaje = int(input(f"introduce el porcentaje del número: {numero} que quieres obtener: "))

operacion = (numero * (porcentaje/100))

print(f"El {porcentaje} % de {numero} es: {operacion}")