from pathlib import Path


carpeta = Path(__file__).resolve().parent
ventas = [45000, 120000, 8000, 300000]
archivo_ventas = carpeta / "ventas.txt"

with archivo_ventas.open("w", encoding="utf-8") as archivo:
    for venta in ventas:
        archivo.write(f"{venta}\n")

with archivo_ventas.open("r", encoding="utf-8") as archivo:
    total_ventas = sum(int(linea.strip()) for linea in archivo)

print(f"Total de ventas: {total_ventas}")
