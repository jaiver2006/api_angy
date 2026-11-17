import requests


URL = "https://api.open-meteo.com/v1/forecast"
parametros = {
    "latitude": 2.4419,
    "longitude": -76.6063,
    "current": "temperature_2m,wind_speed_10m",
}

respuesta = requests.get(URL, params=parametros, timeout=10)
respuesta.raise_for_status()
datos = respuesta.json()
actual = datos["current"]
unidades = datos.get("current_units", {})

print("Temperatura:", actual["temperature_2m"], unidades.get("temperature_2m", "°C"))
print("Viento:", actual["wind_speed_10m"], unidades.get("wind_speed_10m", "km/h"))
