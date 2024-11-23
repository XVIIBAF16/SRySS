## Objetivo
I just recently learnt about the SRA public key cryptosystem... or wait, was it supposed to be RSA? Hmmm, I should probably check...

Additional details will be available after launching your challenge instance.

Connect to the program on our server: `nc saturn.picoctf.net 51044`Download the program: [chal.py](https://artifacts.picoctf.net/c/298/chal.py)
## Solución
En este reto nos dan un servidor y un archivo python, asi que los analizamos y nos conectamos al servidor:

```
nc saturn.picoctf.net 51044
anger = 37529415896518364840795966163435518217066335280877415587823373893391422999438
envy = 53450455678757484663020404718975077309784537360840745857348533364159956561249
vainglory?
```

Creamos un script que nos de la solución a lo que se pide:
```
from Crypto.Util.number import isPrime, long_to_bytes
from string import ascii_letters, digits
from itertools import combinations
from sympy import divisors
from math import log2

anger = int(input("anger = "))
envy = int(input("envy = "))
sloth = 65537

ds = divisors(envy * sloth - 1)
primes = [x + 1 for x in ds if isPrime(x + 1)]
correct_size_primes = [x for x in primes if log2(x) // 1 == 127]

valid_plaintexts = []
charset = ascii_letters + digits
for p, q in combinations(correct_size_primes, 2):
    try:
        s = long_to_bytes(pow(anger, envy, p * q)).decode("ascii")
        if all([c in charset for c in s]):
            valid_plaintexts.append(s)
    except Exception:
        continue

print(valid_plaintexts)
```


Ejecutando este script nos pide los valores y nos da la respuesta:
```
python3 sc.py 
anger = 34571424195731528894956109159638204339391847622689406161646989221541049656178
envy = 59119417767270565859940844359079686627832270996570861894706727697145845585953
['XyQ9shJiio4ehTpx']
```


Ahora este resultado se lo pasamos al servidor:
```
nc saturn.picoctf.net 56276
anger = 34571424195731528894956109159638204339391847622689406161646989221541049656178
envy = 59119417767270565859940844359079686627832270996570861894706727697145845585953
vainglory?
> XyQ9shJiio4ehTpx
XyQ9shJiio4ehTpx
Conquered!
picoCTF{7h053_51n5_4r3_n0_m0r3_b2f9b414}
```

Flag:
```
picoCTF{7h053_51n5_4r3_n0_m0r3_b2f9b414}
```
## Notas adicionales
## Referencias