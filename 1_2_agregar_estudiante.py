from pathlib import Path


archivo_estudiantes = Path(__file__).resolve().parent / "estudiantes.txt"
with archivo_estudiantes.open("a", encoding="utf-8") as archivo:
    archivo.write("Marta\n")

with archivo_estudiantes.open("r", encoding="utf-8") as archivo:
    estudiantes = [linea.strip() for linea in archivo if linea.strip()]

print(f"Cantidad de estudiantes: {len(estudiantes)}")
