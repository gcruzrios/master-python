import os
import shutil
# crear directorios


# Path 
path = "/home/ihritik/Desktop/file(shortcut).txt"
  
  
# Get the canonical path 
# of the specified path 
# by eliminating any symbolic links 
# encountered in the path 
real_path = os.path.realpath(path) 
  
# Print the canonical path 
print(real_path) 



if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")  


#eliminar   

# os.rmdir("./mi_carpeta")


#Copiar

#ruta_original =  "./mi_carpeta"
#ruta_nueva =  "./mi_carpeta_copiado"
#shutil.copytree(ruta_original, ruta_nueva)

os.rmdir("./mi_carpeta")
#os.rmdir("./mi_carpeta_copiado")

print("contenido de mi carpeta")
contenido = os.listdir("./14-sistema-archivos/mi_carpeta")
print (contenido)
