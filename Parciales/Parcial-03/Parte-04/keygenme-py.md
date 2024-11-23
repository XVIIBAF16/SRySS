## Objetivo
[keygenme-trial.py](https://mercury.picoctf.net/static/a6d9cac3bfa4935ceb50c145d3ff5586/keygenme-trial.py)
## Solución
En este reto nos dan un archivo de python, asi que lo analizamos y vemos que nos da un codigo demasiado largo que contiene una parte de la flag pero esta incompleta.

Intentamos conseguir lo que falta de la flag con el script:
```
import hashlib

# Nombre de usuario
username_trial = "PRITCHARD"

# Cálculo del hash SHA-256
hash_val = hashlib.sha256(username_trial.encode()).hexdigest()

# Obtener los caracteres específicos del hash
key_dynamic = hash_val[4] + hash_val[5] + hash_val[3] + hash_val[6] + \
             hash_val[2] + hash_val[7] + hash_val[1] + hash_val[8]

# Parte estática de la clave
key_part_static1 = "picoCTF{1n_7h3_|<3y_of_"
key_part_static2 = "}"
key_full = key_part_static1 + key_dynamic + key_part_static2

print("Clave completa:", key_full)
```

Y ejecutamos:
```
python3 sc.py 
Clave completa: picoCTF{1n_7h3_|<3y_of_54ef6292}
```

Flag:
```
picoCTF{1n_7h3_|<3y_of_54ef6292}
```
## Notas adicionales
## Referencias