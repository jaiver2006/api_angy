import json
from pathlib import Path


archivo_inventario = Path(__file__).resolve().parent / "inventario.json"
with archivo_inventario.open("r", encoding="utf-8") as archivo:
    inventario = json.load(archivo)

inventario.append({"producto": "Bufanda", "precio": 25000, "stock": 15})

with archivo_inventario.open("w", encoding="utf-8") as archivo:
    json.dump(inventario, archivo, indent=4, ensure_ascii=False)

with archivo_inventario.open("r", encoding="utf-8") as archivo:
    inventario_actualizado = json.load(archivo)

print(f"Productos en el inventario: {len(inventario_actualizado)}")
