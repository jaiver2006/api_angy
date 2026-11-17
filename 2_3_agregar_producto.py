import json
from pathlib import Path


# Lee los productos que ya están guardados en el inventario.
archivo_inventario = Path(__file__).resolve().parent / "inventario.json"
with archivo_inventario.open("r", encoding="utf-8") as archivo:
    inventario = json.load(archivo)

# Añade un producto nuevo a la lista existente.
inventario.append({"producto": "Bufanda", "precio": 25000, "stock": 15})

# Guarda la lista actualizada en el archivo JSON.
with archivo_inventario.open("w", encoding="utf-8") as archivo:
    json.dump(inventario, archivo, indent=4, ensure_ascii=False)

# Vuelve a cargar los datos para comprobar cuántos productos quedaron.
with archivo_inventario.open("r", encoding="utf-8") as archivo:
    inventario_actualizado = json.load(archivo)

# Muestra el número total de productos registrados.
print(f"Productos en el inventario: {len(inventario_actualizado)}")
