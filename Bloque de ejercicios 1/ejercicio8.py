"""
Sacar el porciento de un número ingresado por el usuario
"""

valor = int(input("Ingresa un número: "))
porcentaje = int(input("Ingresa el porcentaje a sacar al número: "))

print(f"El {porcentaje}% de {valor} es: {valor*porcentaje/100}")