import json
from pathlib import Path

from clima_utils import consultar_clima


# Solicita las condiciones actuales de Popayán.
clima = consultar_clima(2.4419, -76.6063)
if clima is not None:
    # Guarda la respuesta completa de la API en un archivo JSON.
    archivo_clima = Path(__file__).resolve().parent / "clima.json"
    with archivo_clima.open("w", encoding="utf-8") as archivo:
        json.dump(clima, archivo, indent=4, ensure_ascii=False)

    # Lee el archivo para recuperar y comprobar el dato guardado.
    with archivo_clima.open("r", encoding="utf-8") as archivo:
        clima_guardado = json.load(archivo)

    # Obtiene la temperatura y su unidad; usa °C si la unidad no está informada.
    temperatura = clima_guardado["current"]["temperature_2m"]
    unidad = clima_guardado.get("current_units", {}).get("temperature_2m", "°C")
    print("Temperatura guardada:", temperatura, unidad)
