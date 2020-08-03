from tkinter import *

ventana = Tk()

ventana.geometry("800x600")

ventana.title("ventana de Menu avanzados")

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

archivo = Menu(mi_menu, tearoff=0)
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Nueva ventana")
archivo.add_separator()
archivo.add_command(label="Abrir Archivo")
archivo.add_command(label="Abrir Carpeta")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit)

mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Seleccionar")

ventana.mainloop()
