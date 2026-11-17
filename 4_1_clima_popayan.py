import requests


# Endpoint de Open-Meteo que entrega el pronóstico del clima.
URL = "https://api.open-meteo.com/v1/forecast"
# Coordenadas de Popayán y variables meteorológicas solicitadas.
parametros = {
    "latitude": 2.4419,
    "longitude": -76.6063,
    "current": "temperature_2m,wind_speed_10m",
}

# Consulta la API, valida la respuesta y convierte el resultado a JSON.
respuesta = requests.get(URL, params=parametros, timeout=10)
respuesta.raise_for_status()
datos = respuesta.json()
# Extrae las mediciones actuales y sus unidades (si fueron incluidas).
actual = datos["current"]
unidades = datos.get("current_units", {})

# Muestra la temperatura y la velocidad del viento con sus unidades.
print("Temperatura:", actual["temperature_2m"], unidades.get("temperature_2m", "°C"))
print("Viento:", actual["wind_speed_10m"], unidades.get("wind_speed_10m", "km/h"))
