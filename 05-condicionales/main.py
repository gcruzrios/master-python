"""
Condicional IF

si se cumple condicion

    se ejecutan instrucciones

sino

    Se ejecutan instrucciones



#operadores de comparacion


== igual
!= diferente
<  menor
>  mayor
<= menor igual
>= mayor igual


operadores Lógicos

and y
or  o
!   negacion
not NO

"""




# Ejemplo1 

print("\n===================== EJEMPLO 1 ======================")

color = "rojo"

#color = input ("¿Adivina cuál es mi color favorito:? ")

if color == "rojo":
    print ("Felicidades")
    print ("El color es Rojo")

else:
    print ("El color es incorrecto")


print("\n===================== EJEMPLO 2 ======================")

year = 2020
#year = int(input("¿En que año estamos?"))

if year < 2021:
    print("Estamos antes 2021 !!!")
else:
    print("Estamos en año posterior de 2021")    


print("\n===================== EJEMPLO 3 ======================")

nombre = "Greivin Cruz"
ciudad ="San Jose"
continente="America"
edad =45
mayoria=18

if edad >= mayoria :
    print(f"{nombre} es mayor de edad !!")

    if continente != "Europa":
        print("el usuario NO es de Europa")
    else:
        print(f"Es Europeo y de ciudad {ciudad}")   
else:
    print(f"{nombre} NO es mayor de edad")        


print("\n===================== EJEMPLO 4 ======================")

#dia = int(input ("el número de día de la semana: ?")) 
dia=2
if dia == 1:
     print("Es lunes")
else:
    if dia == 2:
         print("Es Martes")
    else:
        if dia == 3:
            print("Es Miércoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es Fin de Semana")    

#dia = int(input ("el número de día de la semana: ?")) 

dia =1
if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")    
else:
    print("Es Fin de semana")    

print("\n===================== EJEMPLO 5 ======================")

edad_minima = 18
edad_maxima = 65
#edad_oficial = int (input ("Tienes edad trabajar ? Introduce tu edad: "))
edad_oficial = 45

if edad_oficial >= 18 and edad_oficial <= 65: 
    print ("Esta en edad de trabajar !!")
else:
    print ("No está en edad de trabajar")

print("\n===================== EJEMPLO 6 ======================")

pais = "Alemania"

if pais == "Mexico" or pais =="España" or pais =="Colombia":

    print(f" {pais} Es un país de habla hispana !!")
else:
    print(f" {pais} No es un país de habla hispana !!")    


print("\n===================== EJEMPLO 7 ======================")

pais = "España"

if not (pais == "Mexico" or pais =="España" or pais =="Colombia"):

    print(f"{pais} No Es un país de habla hispana !!")
else:
    print(f" {pais} Si es un país de habla hispana !!")  


print("\n===================== EJEMPLO 8 ======================")

pais = "USA"

if  (pais != "Mexico" and pais !="España" and pais !="Colombia"):

    print(f"{pais} No Es un país de habla hispana !!")
else:
    print(f"{pais} Si es un país de habla hispana !!")       