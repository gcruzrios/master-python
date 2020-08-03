# OOP Programación orientada a Objetos

# Definir una clase

# Carro / coche

class Coche:

    #atributos o propiedades
    color = "Rojo"
    marca = "Ferrari"
    modelo ="Aventador"
    velocidad=300
    caballaje=500
    plazas=2

    #metodos o funciones

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self,modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo    

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self): 
        return self.velocidad

    
coche = Coche()

coche.setColor("amarillo")
coche.setModelo("Murcielago")

print(coche.marca, coche.getColor(), coche.getModelo())
print("Velocidad del coche:", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
print("Velocidad nueva del coche:", coche.getVelocidad())



print("-------------------------------------------------------")
# crear mas objetos

coche2 = Coche()
print(coche2.getColor())

coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print(coche2.getColor())

print(coche2.marca, coche2.getColor(), coche2.getModelo())

print(type(coche2))