from tkinter import *

ventana = Tk()

ventana.geometry("800x600")

ventana.title("ventana de prueba")

marco_padre = Frame(ventana, width=250, height=250)
#marco_padre.config(bg="lightblue",bd=3, relief="solid")

marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)


marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="yellow",bd=3, relief="raised")

marco.pack(side=RIGHT, anchor=SE)

marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="green",bd=3, relief="raised")

marco.pack(side=LEFT, anchor=SW)


#------------------------------------

#marco_padre=
#------------------------------------

marco_padre = Frame(ventana, width=250, height=250)
#marco_padre.config(bg="lightblue",bd=3, relief="solid")

marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="blue",bd=3, relief="raised")

marco.pack(side=LEFT, anchor=NE)

marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="orange",bd=3, relief="raised")

marco.pack(side=RIGHT, anchor=NW)
marco.pack_propagate(False)
#Label(marco, text="Primer Marco").pack(side=LEFT,anchor=CENTER)
texto=Label(marco, text="PrimerMarco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial",20),
    height=10,
    width=10,
    bd=3,
    relief=SOLID,
    anchor=CENTER
)

texto.pack(fill=Y, expand=YES)

ventana.mainloop()