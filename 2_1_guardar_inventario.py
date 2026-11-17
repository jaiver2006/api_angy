import json
from pathlib import Path


inventario = [
    {"producto": "Camisa", "precio": 45000, "stock": 20},
    {"producto": "Gorra", "precio": 30000, "stock": 5},
    {"producto": "Pantalón", "precio": 89000, "stock": 12},
    {"producto": "Medias", "precio": 8000, "stock": 40},
    {"producto": "Zapatos", "precio": 150000, "stock": 3},
]

archivo_inventario = Path(__file__).resolve().parent / "inventario.json"
with archivo_inventario.open("w", encoding="utf-8") as archivo:
    json.dump(inventario, archivo, indent=4, ensure_ascii=False)

print(f"Inventario guardado en {archivo_inventario.name}")
