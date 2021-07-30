"""
Ejercicio 2
    Mostrar por pantalla todos los números pares del 1 al 120.
"""
contador = 1

for valor in range(1, 120):
    if valor % 2 == 0:
        print(valor)