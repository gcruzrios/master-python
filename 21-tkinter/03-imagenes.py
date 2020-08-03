from tkinter import *
from PIL import Image, ImageTk



ventana = Tk()

ventana.geometry("700x500")

Label(ventana, text="Hola, soy Victor!!").pack(anchor=W)

ventana.title("ventana de prueba")

imagen = Image.open('./21-tkinter/imagenes/dog1.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()


ventana.mainloop()