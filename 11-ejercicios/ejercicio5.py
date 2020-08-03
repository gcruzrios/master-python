"""
ejercicio 5

"""

#Mostrar un diccionario


tabla = [
    { 
        "categoria":"Accion",
        "juegos": ["GTA", "COD", "PUGB"]

    },
    { 
        "categoria":"Aventura",
        "juegos": ["ASSIN", "CRASH", "PofP"]
        
    },
    { 
        "categoria":"Deportes",
        "juegos": ["FIFA", "PES", "MOTO-GP"]
        
    }
]

for categoria in tabla:

    print(f"--------------{categoria['categoria']}---------------------------")

    for juego in categoria['juegos']:
        print(juego)