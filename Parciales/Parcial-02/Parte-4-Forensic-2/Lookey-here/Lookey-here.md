## Objetivo
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.
Download the data [here](https://artifacts.picoctf.net/c/125/anthem.flag.txt).
## Solución
En este reto nos dan un archivo .txt

Le hacemos un cat y muestra vario texto asi que aplicamos un grep:
```
cat anthem.flag.txt | grep picoCTF
      we think that the men of picoCTF{gr3p_15_@w3s0m3_58f5c024}
```

y nos da la flag
```
picoCTF{gr3p_15_@w3s0m3_58f5c024}
```

## Notas adicionales
## Referencias