"""
Pedir la nota de n alumnos y mostrar en pantalla cuantos pasaron y cuantos no.
"""

aprobados = 0
reprobados = 0

alumnos = int(input("Ingresa la cantidad de alumnos: "))

for i in range(alumnos):
    calificacion = int(input(f"Ingresa la calificación del alumno {i}: "))

    if calificacion <=5:
        reprobados += 1
    else:
        aprobados +=1

print(f"Aprobaron {aprobados} alumnos.\nReprobaron {reprobados} alumnos")