"""
Crear un programa que tenga 4 variables y decir el tipo de datos que tenga una variable.
    - String
    - Entero
    - List
    - Bool
"""

cadena = "Este es un texto"
numero = 34
lista = [2, 4, "Hola", "Mundo"]
verificacion = True

def translate_type(type):
    if type == str:
        return "String"
    elif type == int:
        return "Entero"
    elif type == list:
        return "Lista"
    elif type == bool:
        return "Boolean"

def verify_data(elem):
    tipo = type(elem)
    print(f"El dato {elem} es de tipo {translate_type(tipo)}")

verify_data(cadena)
verify_data(numero)
verify_data(lista)
verify_data(verificacion)