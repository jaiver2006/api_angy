from pathlib import Path

# Obtiene la carpeta donde está este script para guardar el archivo junto a él.
carpeta = Path(__file__).resolve().parent
# Lista de importes de ventas que se van a registrar.
ventas = [45000, 120000, 8000, 300000]
# Construye la ruta del archivo de texto dentro de la carpeta del script.
archivo_ventas = carpeta / "ventas.txt"

# Abre el archivo para escribir y guarda cada venta en una línea.
with archivo_ventas.open("w", encoding="utf-8") as archivo:
    for venta in ventas:
        archivo.write(f"{venta}\n")

# Lee los importes guardados, los convierte a enteros y calcula su suma.
with archivo_ventas.open("r", encoding="utf-8") as archivo:
    total_ventas = sum(int(linea.strip()) for linea in archivo)

# Muestra en pantalla el total de las ventas registradas.
print(f"Total de ventas: {total_ventas}")
