## Objetivo
We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) `lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil` [new_caesar.py](https://mercury.picoctf.net/static/c9043977604318594ab73d126a01d0b1/new_caesar.py)
## Solución
En este reto nos dan un archivo python el cual debemos ejecutar pasándole el string que es la bandera encriptada:

Creamos un nuevo script:
```
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(enc):
    plain = ""
    for c1, c2 in zip(enc[0::2], enc[1::2]):
        n1 = "{0:04b}".format(ALPHABET.index(c1))
        n2 = "{0:04b}".format(ALPHABET.index(c2))
        binary = int(n1 + n2, 2)
        plain += chr(binary)
    return plain

def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

def decrypt(enc, key):
    dec = ""
    for i, c in enumerate(enc):
        dec += unshift(c, key[i % len(key)])
    return dec

ciphertext = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"

for k in ALPHABET:
    decrypted = decrypt(ciphertext, k)
    if all([c in ALPHABET for c in decrypted]):
        decoded = b16_decode(decrypted)
        if all([c in string.printable for c in decoded]):
            print(f"Key: {k}, Plaintext: {decoded}")
```

Lo ejecutamos:
```
python3 flag.py
Key: f, Plaintext: et_tu?_431db62c5618cd75f1d0b83832b67b46
Key: g, Plaintext: TcNcd.N#" SQ%!R$% 'RS&$U S/Q'"'"!Q%&Q#%
```

Y nos da la flag:
```
picoCTF{et_tu?_431db62c5618cd75f1d0b83832b67b46}
```
## Notas adicionales
## Referencias