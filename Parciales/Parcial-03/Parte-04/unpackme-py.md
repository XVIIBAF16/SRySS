## Objetivo
Can you get the flag?
Reverse engineer this [Python program](https://artifacts.picoctf.net/c/50/unpackme.flag.py).
## Solución
En este reto nos dan un archivo en python asi que lo analizamos con cat:

```
import base64
from cryptography.fernet import Fernet



payload = b'gAAAAABkzWGWvEp8gLI9AcIn5o-ahDUwkTvM6EwF7YYMZlE-_Gf9rcNYjxIgX4b0ltY6bcxKarib2ds6POclRwCwhsRb1LOXVt4Q3ePtMY4BmHFFZlIHLk05CjwigT7hiI9p3sH9e7Cpk1uO90xbHbuy-mfi3nkmn411aBgwxyWpJvykpkuBIG_nty6zbox3UhbB85TOis0TgM0zG4ht0-GUW4wTq2_5-wkw3kV1ZAisLJHzF-Z9oLMmwFZU0UCAcHaBTGDF5BnVLmUeCGTgzVLSNn6BmB61Yg=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
```

Examinando el codigo hacemos un nuevo script:
```
import base64
from cryptography.fernet import Fernet

# The encrypted payload (from your provided code)
payload = b'gAAAAABkzWGWvEp8gLI9AcIn5o-ahDUwkTvM6EwF7YYMZlE-_Gf9rcNYjxIgX4b0ltY6bcxKarib2ds6POclRwCwhsRb1LOXVt4Q3ePtMY4BmHFFZlIHLk05CjwigT7hiI9p3sH9e7Cpk1uO90xbHbuy-mfi3nkmn411aBgwxyWpJvykpkuBIG_nty6zbox3UhbB85TOis0TgM0zG4ht0-GUW4wTq2_5-wkw3kV1ZAisLJHzF-Z9oLMmwFZU0UCAcHaBTGDF5BnVLmUeCGTgzVLSNn6BmB61Yg=='

# The key in base64 (it was provided in the script)
key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())

# Use Fernet to decrypt the payload
f = Fernet(key_base64)

# Decrypt the payload
plain = f.decrypt(payload)

# The decrypted content is executed by the original script
# Let's print the decrypted string to see what it contains
print(plain.decode())
```

Ejecutamos:
```
python3 sc.py 

pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_85f5d0ac}')
else:
  print('That password is incorrect.')
```

Flag:
```
picoCTF{175_chr157m45_85f5d0ac}
```
## Notas adicionales
## Referencias