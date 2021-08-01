"""
Crear una lista con el contenido de una tabla:
* Accion: GTA, Cod, Pugb
* Aventura: assins, crash, prince of persia
* Deportes: fifa 21, pro 21, moto gp 21
"""

tabla = [
    {
        "categoria": "accion",
        "lista": ["GTA", "COD", "PUGB"]
    },
    {
        "categoria": "Aventura",
        "lista": ["Assins", "Crash", "Prince Of Persia"]
    },
    {
        "categoria": "Deporte",
        "lista": ["Fifa 21", "PRO 21", "Moto Gp 21"]
    }

]

for categoria in tabla:
    print(f"Categoría: {categoria['categoria']}")
    for game in categoria['lista']:
        print(f"\t{game}")

