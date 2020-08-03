"""
Variables boolean

4 variables

1. lista. 2. String, 3, entero, 4 boolean

"""
def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "String"
    elif tipo == int:
        result = "Integer"
    elif tipo == bool:
        result = "boolean"
    return result

def comprobarTipoDato(dato, tipo):
    test = isinstance(dato,tipo)
    result = ""

    if test:
        print(f"Este dato es del tipo {type(dato)}")
        print(f"Este dato es del tipo {traducirTipo(tipo)}")
    else: 
        #result = None 
        result = "No es tipo correcto"
    return result

mi_lista = ["hola mundo", 88]
titulo = "Master en Python"
numero = 100
verdadero = True

print(comprobarTipoDato(mi_lista, list))
print(comprobarTipoDato(titulo, str))
print(comprobarTipoDato(numero, int))
print(comprobarTipoDato(verdadero, bool))
