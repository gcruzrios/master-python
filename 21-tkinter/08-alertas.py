from tkinter import *
from tkinter import messagebox as MessageBox


ventana = Tk()

ventana.geometry("800x600")

ventana.title("Formularios")

def sacarAlerta():
    MessageBox.showinfo("Alerta", "Hola soy Greivin Cruz")
    #MessageBox.showwarning("Alerta", "Hola soy Greivin Cruz")
    #MessageBox.showerror("Alerta", "Hola soy Greivin Cruz")

Button(ventana, text="Mostrar alerta", command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "Continuar con la aplicación ? ")

    if resultado != "yes":
        MessageBox.showinfo("Adios", f" Adios {nombre}")
        ventana.destroy()


Button(ventana, text="Salir", command= lambda: salir("Greivin Cruz")).pack()

ventana.mainloop()