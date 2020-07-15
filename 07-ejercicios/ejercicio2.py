"""
Numeros pares de 1 a 120
"""

contador =1

for contador in range (1, 121):
    if contador%2 == 0:
        print(f"{contador} es par")
    else:
        print(f"{contador} es impar")