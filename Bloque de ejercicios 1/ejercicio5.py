"""
Mostrar todos los números dentro de un rango. Inicio - rango con entradas desde el usuario
"""

inicio = int(input("Ingresa el inicio del rango: "))
fin = int(input("Ingresa el final del rango: "))

print(f"Los números dentro del rango {inicio} - {fin} son")

if inicio >= fin:
    print("El primero número debe ser menor al segundo")
else:
    for valor in range(inicio+1, fin):
        print(valor)