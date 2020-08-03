
# CalCulaDORA CON tKiNTER

from tkinter import *
from tkinter import messagebox as MessageBox


ventana = Tk()
ventana.geometry("800x600")
ventana.title("Formulario Calculadora ")

def cFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        MessageBox.showerror("Error", "Ingresa bien los datos")
    return result    
def sumar():
    
    resultado.set(cfloat(numero1.get()) + cfloat(numero2.get()))
    mostrarResultado()
    
def restar():
    
    resultado.set(cfloat(numero1.get()) - cfloat(numero2.get()))
    mostrarResultado()
      

def multiplicar():
    
    resultado.set(cfloat(numero1.get()) * cfloat(numero2.get()))
    mostrarResultado()  
         

def dividir():
       
    resultado.set(cfloat(numero1.get()) / cfloat(numero2.get()))
    mostrarResultado()
    
def mostrarResultado():
    MessageBox.showinfo("Resultado", f"El resultado es: {resultado.get()}")
    numero1.set("")
    numero2.set("")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=450, height= 380)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID

)
marco.pack(side=TOP, anchor=CENTER)


Label(marco, text="Primer número").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo número").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text ="").pack()

Button(marco, text="Sumar", command=sumar).pack(side='left', fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side='left', fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side='left', fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side='left',fill=X, expand=YES)


ventana.mainloop()
