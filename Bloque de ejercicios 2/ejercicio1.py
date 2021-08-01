"""
Hacer un programa que tenga una lista de enteros que tenga 8 elementos y hacer lo siguiente:
    - Recorrer la lista y mostrarla
        - Hacerlo en una función devolviendo un String
    - Ordenarla y mostrarla
    - Mostrar su longitud
    - Buscar un elemento que el usuario pida
"""

numeros = [13, 64, 52, 73, 21, 7, 91, 64]

# Recorrer y mostrar la lista
def showList(list):
    result = ""
    for elem in list:
        result += str(elem) + "\n"
    return result

print("La lista es:\n" + showList(numeros))

# Ordenar y mostrar la lista
numeros.sort()
print("La lista ordenada es:\n" + showList(numeros))

# Mostrar la longitud
print("La longitud de la lista es: " + str(len(numeros)))

# Buscar un elemento que el usuario pida
num = int(input("Ingresa el numero que quieres buscar: "))
index = numeros.index(num)
print("El número que buscas está en la posición: " + str(index))
