"""
Programa que compruebe si una variable está vacía.
De ser así, rellenarla con texto y mostrarlo en mayúsculas.
"""

entry = ""

while len(entry) == 0:
    entry = input("Ingresa un text: ")

print(f"El texto es: {entry.upper()}")