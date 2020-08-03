from coche import Coche

carro=Coche("Azul", "Toyota", "Yaris",200,200,5)
carro2=Coche("Verde", "Seat", "Panda",230,210,5)
carro3=Coche("Rojo", "Mercedez", "Clase A",210,23,4)


print(carro.getColor())

print(carro.getInfo())

print(carro2.getInfo())

print(carro3.getInfo())

# detectar tipado

if type(carro3) == Coche:
    print("Es el objeto coche")
else:
    print("No es un objeto")    


#Visibilidad

print(carro.soy_publico) 

print(carro.getPrivado())