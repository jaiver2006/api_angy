from pathlib import Path


archivo = Path(__file__).resolve().parent / "no_existe.txt"
try:
    with archivo.open("r", encoding="utf-8") as entrada:
        print(entrada.read())
except FileNotFoundError:
    print("El archivo no existe. Revisa el nombre o la carpeta.")
