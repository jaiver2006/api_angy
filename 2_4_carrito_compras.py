import json
from pathlib import Path
from typing import Any


CARPETA = Path(__file__).resolve().parent


class CarritoCompras:
    def __init__(self) -> None:
        self.productos: list[dict[str, Any]] = []

    def guardar(self, archivo: str) -> None:
        ruta = CARPETA / archivo
        with ruta.open("w", encoding="utf-8") as salida:
            json.dump(self.productos, salida, indent=4, ensure_ascii=False)

    def cargar(self, archivo: str) -> None:
        ruta = CARPETA / archivo
        with ruta.open("r", encoding="utf-8") as entrada:
            productos = json.load(entrada)
        if not isinstance(productos, list):
            raise ValueError("El archivo del carrito debe contener una lista JSON.")
        self.productos = productos


primer_carrito = CarritoCompras()
primer_carrito.productos = [
    {"producto": "Camisa", "cantidad": 2, "precio": 45000},
    {"producto": "Gorra", "cantidad": 1, "precio": 30000},
]
segundo_carrito = CarritoCompras()

primer_carrito.guardar("carrito.json")
segundo_carrito.cargar("carrito.json")
print("Productos cargados en el segundo carrito:", segundo_carrito.productos)
