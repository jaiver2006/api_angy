import json
from pathlib import Path

from clima_utils import consultar_clima


ciudades = {
    "Popayán": (2.4419, -76.6063),
    "Bogotá": (4.7110, -74.0721),
    "Cali": (3.4516, -76.5320),
    "Medellín": (6.2442, -75.5812),
}
temperaturas: dict[str, float] = {}

for ciudad, (latitud, longitud) in ciudades.items():
    clima = consultar_clima(latitud, longitud)
    if clima is None:
        print(f"Se omitirá {ciudad} porque no se pudo consultar.")
        continue
    temperaturas[ciudad] = clima["current"]["temperature_2m"]

archivo_temperaturas = Path(__file__).resolve().parent / "clima_ciudades.json"
with archivo_temperaturas.open("w", encoding="utf-8") as archivo:
    json.dump(temperaturas, archivo, indent=4, ensure_ascii=False)

with archivo_temperaturas.open("r", encoding="utf-8") as archivo:
    temperaturas_guardadas = json.load(archivo)

if temperaturas_guardadas:
    ciudad_mas_calida = max(temperaturas_guardadas, key=temperaturas_guardadas.get)
    print(
        f"La ciudad más calurosa es {ciudad_mas_calida} "
        f"({temperaturas_guardadas[ciudad_mas_calida]} °C)."
    )
else:
    print("No se obtuvieron temperaturas para comparar.")
