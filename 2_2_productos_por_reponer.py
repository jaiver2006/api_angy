import json
from pathlib import Path


# Ubica y carga el inventario guardado en formato JSON.
archivo_inventario = Path(__file__).resolve().parent / "inventario.json"
with archivo_inventario.open("r", encoding="utf-8") as archivo:
    inventario = json.load(archivo)

# Recorre los productos e informa cuáles tienen menos de 10 unidades.
print("Productos con stock menor a 10:")
for producto in inventario:
    if producto["stock"] < 10:
        print(f"- {producto['producto']}: {producto['stock']} unidades")
