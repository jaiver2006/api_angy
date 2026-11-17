from typing import Any

import requests


URL_CLIMA = "https://api.open-meteo.com/v1/forecast"


def consultar_clima(lat: float, lon: float) -> dict[str, Any] | None:
    parametros = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m",
    }
    try:
        respuesta = requests.get(URL_CLIMA, params=parametros, timeout=10)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as error:
        print(f"No se pudo consultar el clima: {error}")
        return None


def imprimir_clima(datos: dict[str, Any]) -> None:
    actual = datos["current"]
    unidades = datos.get("current_units", {})
    print("Temperatura:", actual["temperature_2m"], unidades.get("temperature_2m", "°C"))
    print("Viento:", actual["wind_speed_10m"], unidades.get("wind_speed_10m", "km/h"))
