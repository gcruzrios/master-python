from tkinter import *
import os.path

class Programa:
 
    def __init__(self):
        self.title = "Ventana de prueba"
        self.icon = os.path.abspath('./21-tkinter/Coffee.ico')
        self.icon_alt = os.path.abspath('./21-tkinter/Coffee.ico')
        self.size = "750x475"
        self.resizable = False

    def cargar(self):
        ventana = Tk()
        self.ventana = ventana
        ventana.title(self.title)
        #tamaño de la ventana
        ventana.geometry(self.size)

        #comprobar si existe archivo
        ruta_icono = os.path.abspath('./21-tkinter/imagenes/Coffee.ico')
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath('./imagenes/Coffee.ico')

        #ventana.iconbitmap(ruta_icono)
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)

        


    def addTexto(self,dato):
        texto = Label(self.ventana,text=dato)
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()

programa = Programa()
programa.cargar()
programa.addTexto("Hola soy un texto")
programa.addTexto("Greivin Cruz")
programa.addTexto("Sigueme en twitter")


programa.mostrar()