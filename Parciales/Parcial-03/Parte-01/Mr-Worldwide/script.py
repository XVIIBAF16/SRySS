import requests
import re

# Flag con coordenadas geográficas
flag = "picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}"

# Función para obtener una letra desde la API
def get_letter_from_coordinate(match):
    lat = match.group(1)
    long = match.group(2)
    url = f"https://geocode.xyz/{lat},{long}?json=1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        city = data.get("city", "UNKNOWN")
        return city[0].upper() if city else "?"
    except Exception as e:
        print(f"Error con coordenadas ({lat}, {long}): {e}")
        return "?"

# Reemplaza coordenadas en el flag por las letras correspondientes
processed_flag = re.sub(r'\(([\d\.-]+), ([\d\.-]+)\)', get_letter_from_coordinate, flag)

print(processed_flag)
import requests
import re

# Flag con coordenadas geográficas
flag = "picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}"

# Función para obtener una letra desde la API
def get_letter_from_coordinate(match):
    lat = match.group(1)
    long = match.group(2)
    url = f"https://geocode.xyz/{lat},{long}?json=1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        city = data.get("city", "UNKNOWN")
        return city[0].upper() if city else "?"
    except Exception as e:
        print(f"Error con coordenadas ({lat}, {long}): {e}")
        return "?"

# Reemplaza coordenadas en el flag por las letras correspondientes
processed_flag = re.sub(r'\(([\d\.-]+), ([\d\.-]+)\)', get_letter_from_coordinate, flag)

print(processed_flag)

