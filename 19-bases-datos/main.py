import mysql.connector

database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="12345678",
    database="master_python"
)
#print(database)

cursor = database.cursor(buffered=True)

#crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

for db in cursor:
    print(db)

#crear tablas   

cursor.execute ("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

for table in cursor:
    print(table)

#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")

coches = [
    ('Seat','Ibiza',5000),
    ('Seat','Panda',4000),
    ('Renault','Clio',15100),
    ('Toyota','Yaris',15000),
    ('Citroen','Saxo',25000),
    ('Mercedes','Clase C',35000),
]

#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)

cursor.execute("SELECT * FROM vehiculos WHERE precio <= 25000 AND marca='Seat'" )

result = cursor.fetchall()
print("Todos los coches")
for coche in result:
    print(coche[1], coche[3])



cursor.execute("SELECT * FROM vehiculos" )
coche = cursor.fetchone()
print(coche)


cursor.execute("DELETE FROM vehiculos WHERE marca='Renault'")

print(cursor.rowcount, "borrados !!")


cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE modelo='Panda'")

database.commit()