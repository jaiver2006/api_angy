from pathlib import Path

# Construye la ruta al archivo de estudiantes junto a este script.
archivo_estudiantes = Path(__file__).resolve().parent / "estudiantes.txt"
# Agrega el nuevo nombre al final del archivo sin borrar los anteriores.
with archivo_estudiantes.open("a", encoding="utf-8") as archivo:
    archivo.write("Marta\n")

# Lee los nombres no vacíos y elimina el salto de línea de cada uno.
with archivo_estudiantes.open("r", encoding="utf-8") as archivo:
    estudiantes = [linea.strip() for linea in archivo if linea.strip()]

# Informa cuántos estudiantes hay registrados.
print(f"Cantidad de estudiantes: {len(estudiantes)}")
