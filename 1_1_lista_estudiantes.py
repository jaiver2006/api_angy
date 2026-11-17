from pathlib import Path


carpeta = Path(__file__).resolve().parent
estudiantes = ["Carlos", "Ana", "Luis", "david"]

with (carpeta / "estudiantes.txt").open("w", encoding="utf-8") as archivo:
    for nombre in estudiantes:
        archivo.write(nombre + "\n")

with (carpeta / "estudiantes.txt").open("r", encoding="utf-8") as archivo:
    for numero, linea in enumerate(archivo, start=1):
        print(numero, linea.strip())
