"""
Mostrar todos los números impares que se encuentre entre un
rango específico que decida el usuario.
"""

inicio = int(input("Ingresa el inicio del rango: "))
fin = int(input("Ingresa el fin del rango: "))

for val in range(inicio, fin):
    if val%2 == 1:
        print(val)