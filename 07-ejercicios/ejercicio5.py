# Numeros entre rango ingresado en variables del input

numero1= int(input("introduce el primer número: "))
numero2= int(input("introduce el segundo número: "))

if numero1 < numero2:
    for contador in range(numero1, (numero2+1)):
        print(contador)

else:
    print("El número 1 5debe ser mayor al número 2")