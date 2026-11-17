from typing import Any

import requests


URL_CLIMA = "https://api.open-meteo.com/v1/forecast"


# Consulta Open-Meteo para unas coordenadas y devuelve sus datos actuales.
def consultar_clima(lat: float, lon: float) -> dict[str, Any] | None:
    # Solicita temperatura y velocidad del viento para la ubicación.
    parametros = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m",
    }
    try:
        # Envía la petición, comprueba errores HTTP y obtiene la respuesta JSON.
        respuesta = requests.get(URL_CLIMA, params=parametros, timeout=10)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as error:
        # Informa de fallos de conexión o respuesta y señala que no hubo datos.
        print(f"No se pudo consultar el clima: {error}")
        return None


# Muestra temperatura y viento usando las unidades incluidas en la respuesta.
def imprimir_clima(datos: dict[str, Any]) -> None:
    actual = datos["current"]
    unidades = datos.get("current_units", {})
    print("Temperatura:", actual["temperature_2m"], unidades.get("temperature_2m", "°C"))
    print("Viento:", actual["wind_speed_10m"], unidades.get("wind_speed_10m", "km/h"))
