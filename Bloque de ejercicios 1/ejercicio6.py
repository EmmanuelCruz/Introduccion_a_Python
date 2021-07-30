"""
Mostrar todas las tablas de múltiplicar del 1 al 10
"""

for val1 in range(1, 11):
    print(f"\nTABLA DEL {val1}")
    for val2 in range(1, 11):
        print(f"{val1} x {val2} = {val1*val2}")
    