## Objetivo
A musician left us a [message](https://jupiter.challenges.picoctf.org/static/d5570d48262dbba2a31f2a940409ad9d/message.txt). What's it mean?
## Solución
En este reto nos dan un archivo que al parecer contiene la flag cifrada:
```
cat message.txt 
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
```


Al parecer son coordenadas asi que intentamos descifrar usando un script en python:
```
import requests
import re

flag = "picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}"

def get_letter_from_coordinate(match):
    lat = match.group(1)
    long = match.group(2)
    r = requests.get(f"https://geocode.xyz/{lat},{long}?json=1")
    j = r.json()
    return j.get("geocode", [""])[0]

print(re.sub(r'\(([\d\.-]+), ([\d\.-]+)\)', get_letter_from_coordinate, flag))

```

Lo ejecutamos:
```
python3 script.py 
picoCTF{KODIAK_ALASKA}
```

y nos da la flag:
```
picoCTF{KODIAK_ALASKA}
```
## Notas adicionales
## Referencias