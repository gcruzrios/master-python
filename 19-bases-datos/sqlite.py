import sqlite3

#Conexion

conexion = sqlite3.connect('./19-bases-datos/pruebas.db')



#crear cursor

cursor = conexion.cursor()

#crear tabla

cursor.execute("CREATE TABLE IF NOT EXISTS productos (" +
"id INTEGER PRIMARY KEY AUTOINCREMENT," +
"titulo varchar(255),"+
"descripcion text,"+
"precio int(255)"+
")")

conexion.commit()

# Insertar


# cursor.execute("INSERT INTO productos VALUES(null, 'Primer Producto','Descripcion de mi producto', 550)")

conexion.commit()

# Borrar registros
cursor.execute("DELETE FROM productos where id != 1 ")
# listar datos


    
cursor.execute("SELECT * FROM productos;")   
producto = cursor.fetchone()
print(producto)



#Insertar muchos registros

productos = [
    ("PC laptop", "Buen PC", 600),
    ("telefono movil", "Buen telefono", 100),
    ("Placa Base", "Buena Placa", 200),
    ("Tablet 15", "Buena Tablet", 400)
]

cursor.executemany("INSERT INTO productos VALUES (null, ?,?,?)", productos)

cursor.execute("UPDATE productos SET precio = 654 WHERE productos.id=1")

cursor.execute("SELECT * FROM productos WHERE precio > 200;")

productos = cursor.fetchall()

for producto in productos:
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

#Update






#cerrar conexion
conexion.close()

