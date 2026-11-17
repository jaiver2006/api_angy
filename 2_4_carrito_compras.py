import json
from pathlib import Path
from typing import Any


# Usa la carpeta del script como ubicación base de los archivos del carrito.
CARPETA = Path(__file__).resolve().parent


class CarritoCompras:
    def __init__(self) -> None:
        # Cada instancia mantiene su propia lista de productos.
        self.productos: list[dict[str, Any]] = []

    def guardar(self, archivo: str) -> None:
        # Guarda los productos de este carrito en un archivo JSON.
        ruta = CARPETA / archivo
        with ruta.open("w", encoding="utf-8") as salida:
            json.dump(self.productos, salida, indent=4, ensure_ascii=False)

    def cargar(self, archivo: str) -> None:
        # Lee los datos y verifica que el contenido JSON sea una lista.
        ruta = CARPETA / archivo
        with ruta.open("r", encoding="utf-8") as entrada:
            productos = json.load(entrada)
        if not isinstance(productos, list):
            raise ValueError("El archivo del carrito debe contener una lista JSON.")
        # Reemplaza el contenido del carrito con los productos leídos.
        self.productos = productos


# Crea dos carritos y agrega productos al primero.
primer_carrito = CarritoCompras()
primer_carrito.productos = [
    {"producto": "Camisa", "cantidad": 2, "precio": 45000},
    {"producto": "Gorra", "cantidad": 1, "precio": 30000},
]
segundo_carrito = CarritoCompras()

# Guarda el primer carrito y carga esos datos en el segundo.
primer_carrito.guardar("carrito.json")
segundo_carrito.cargar("carrito.json")
# Muestra los productos cargados en el segundo carrito.
print("Productos cargados en el segundo carrito:", segundo_carrito.productos)
