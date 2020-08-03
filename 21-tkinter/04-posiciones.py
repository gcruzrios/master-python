from tkinter import *

ventana = Tk()

ventana.geometry("800x600")


texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="black",
    padx=20,
    pady=20,
    font=("Arial",12)
    )
texto.pack()


texto = Label(ventana, text="Soy Greivin Cruz")
texto.config(
    fg="black",
    bg="orange",
    padx=20,
    pady=20,
    font=("Arial",12),
    #width=400,
    height=10,
    cursor="circle"

    )
texto.pack(side=TOP, fill=X, expand=YES)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

texto = Label(ventana, text=pruebas(nombre="Greivin",apellidos="Cruz",pais="Costa Rica"))
texto.config(
    fg="black",
    bg="orange",
    padx=20,
    pady=20,
    font=("Arial",12),
    #width=320,
    height=3,
    cursor="circle"

    )
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text=pruebas(nombre="Victor",apellidos="Robles",pais="España"))
texto.config(
    fg="black",
    bg="red",
    padx=20,
    pady=20,
    font=("Arial",12),
    #width=320,
    height=3,
    cursor="circle"

    )
texto.pack(side=LEFT,fill=X, expand=YES)
texto = Label(ventana, text=pruebas(nombre="Victor",apellidos="Robles",pais="España"))
texto.config(
    fg="black",
    bg="green",
    padx=20,
    pady=20,
    font=("Arial",12),
    #width=320,
    height=3,
    cursor="circle"

    )
texto.pack(side=LEFT, fill=X, expand=YES )



texto.pack(side=TOP)



ventana.mainloop()