"""
Escribir un programa que añada valores a una lista mientras
su longitud sea menor a 12 y mostrar la lista
    - Hacerlo con while
    - Hacerlo con for
"""

lista = []

while len(lista) < 12:
    entrada = input("Ingresa un dato: ")
    lista.append(entrada)

print(f"La lista es: {lista}")

lista2 = []
for elem in range(12):
    entrada2 = input("Ingresa un dato: ")
    lista2.append(entrada2)

print(f"La lista es: {lista2}")