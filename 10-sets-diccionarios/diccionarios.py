"""
Es un tipo de datos en formato conjunto de datos
en formato clave > valor
Es parecido a array asociativo o un objeto JSON

"""
persona = {
    "nombre":"Greivin",
    "apellidos":"Cruz",
    "web":"greivin.net"
}

print (persona["web"])

#Lista de diccionarios

contactos = [
    {
        "nombre":"Antonio",
        "email":"tony@correo.com"
    },
    {
        "nombre":"Salvador",
        "email":"salvatrucho@correo.com"
    },
    {
        "nombre":"Luis",
        "email":"luis@correo.com"
    }
    
]

contactos[0]['nombre'] = "Antoñito"

print(contactos[0]['nombre'])

for contacto in contactos:
    print(f"Nombre de contacto: {contacto['nombre']}")
    print(f"Email de contacto: {contacto['email']}")
    print("---------------------------------------------")
