class Coche:

    #atributos o propiedades
    color = "Rojo"
    marca = "Ferrari"
    modelo ="Aventador"
    velocidad=300
    caballaje=500
    plazas=2

    #metodos o funciones

    soy_publico ="Soy un atributo público"
    __soy_privado ="Soy un atributo privado"


    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color= color
        self.marca= marca
        self.modelo= modelo
        self.velocidad= velocidad
        self.caballaje= caballaje
        self.plazas= plazas

    def getPrivado(self):
        return self.__soy_privado

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self,modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo    


    def setMarca(self,marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self): 
        return self.velocidad

    def getInfo(self):
        info = "-------------------------Info del carro---------------------------"
        info += "\n color " + self.getColor()
        info += "\n marca " + self.getMarca()
        info += "\n modelo " + self.getModelo()
        info += "\n velocidad " + str(self.getVelocidad())
        
        return info