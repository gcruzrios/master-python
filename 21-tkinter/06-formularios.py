from tkinter import *

ventana = Tk()

ventana.geometry("800x600")

ventana.title("Formularios")

#Encabezado

encabezado = Label(ventana, text="Formularios con Tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans",18),
    padx=10,
    pady=10
)

#encabezado.pack(side=LEFT,anchor=NW, fill=X, expand=YES )
encabezado.grid(row=0, column=0, columnspan=2, sticky=W)

#Label (nombre)
label=Label(ventana, text="Nombre :")
label.grid(row=1,column=0,padx=5, pady=5)

#campo de texto (nombre)

campo_texto = Entry(ventana)
campo_texto.grid(row=1,column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")
#campo_texto.pack(side=LEFT, anchor=W)


#Label (apellidos)
label=Label(ventana, text="Apellidos :")
label.grid(row=2,column=0,padx=5, pady=5)

campo_texto = Entry(ventana)
campo_texto.grid(row=2,column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal") # state="disabled"


#Label (apellidos)
label=Label(ventana, text="Descripción :")
label.grid(row=3,column=0,padx=5, pady=5, sticky=NE)

campo_grande = Text(ventana)
campo_grande.grid(row=3,column=1)
campo_grande.config(
    width=30,
    height=5,
    font=("Arial",12),
    padx=15,
    pady=15
)

#Botones
Label(ventana).grid(row=4, column=1)

boton= Button(ventana, text="Enviar")
boton.grid(row=4,column=1,sticky=W)
boton.config(padx=15, pady=15, bg="green", fg="white")

ventana.mainloop()
