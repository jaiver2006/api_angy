import json
from pathlib import Path


archivo_inventario = Path(__file__).resolve().parent / "inventario.json"
with archivo_inventario.open("r", encoding="utf-8") as archivo:
    inventario = json.load(archivo)

print("Productos con stock menor a 10:")
for producto in inventario:
    if producto["stock"] < 10:
        print(f"- {producto['producto']}: {producto['stock']} unidades")
