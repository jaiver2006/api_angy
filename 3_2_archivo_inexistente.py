from pathlib import Path


# Prepara la ruta del archivo que se intentará leer.
archivo = Path(__file__).resolve().parent / "no_existe.txt"
try:
    # Abre el archivo y muestra su contenido si está disponible.
    with archivo.open("r", encoding="utf-8") as entrada:
        print(entrada.read())
except FileNotFoundError:
    # Informa de forma clara si el archivo no existe en esa ubicación.
    print("El archivo no existe. Revisa el nombre o la carpeta.")
