from io import open
import pathlib
import shutil

import os
import os.path

ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

print(ruta)

# archivo = open(ruta, "a+")

# escribir en el archivo

# archivo.write("**********************SOY UN TEXTO DESDE PYTHON **************************\n")

# archivo.close()



# leer contenido

#ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

#archivo_lectura = open(ruta, "r")

#contenido =  archivo_lectura.read()
#print(contenido)

# leer contenido y guardar en lista

#lista = archivo_lectura.readlines()

#archivo_lectura.close()

#for frase in lista:

#    if not frase.isnumeric():
#      print ("-" + frase.upper())


#copiar

# ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_copiado.txt"
# shutil.copyfile(ruta_original, ruta_nueva)



#Mover

#ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto_copiado.txt"
#ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_copiado2.txt"

#shutil.move(ruta_original, ruta_nueva)

# Eliminar 
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_copiado2.txt"
#os.remove(ruta_nueva)

print(os.path.abspath("./"))

if os.path.isfile(os.path.abspath("./")+"/fichero_texto.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")

