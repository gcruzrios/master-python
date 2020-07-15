frase="Ni Victor Robles es Fernando Herrera, ni Fernando Herrera es Victor Robles"

print(frase)

def holaMundo():

    frase = "Hola mundo !!"
    print(frase)
    year = 2021
    print(year)
    #return year
    global website
    website = "greivin.net"
    print ("Dentro: ", website)
    return "Dato devuelto " + str(year)
holaMundo()    
print(holaMundo())
print("Fuera: ", website)