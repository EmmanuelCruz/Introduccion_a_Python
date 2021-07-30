"""
Imprimir los cuadrados de los primeros 60 naturales.
    - Resolver con for
    - Resolver con while
"""

# Solución con FOR

for valor in range(1, 61):
    print(f"El cuadrado de {valor} es {valor*valor}")

# Solución con while
contador = 1
while contador <= 60:
    print(f"El cuadrado de {contador} es {contador*contador}")
    contador += 1