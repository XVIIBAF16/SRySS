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

