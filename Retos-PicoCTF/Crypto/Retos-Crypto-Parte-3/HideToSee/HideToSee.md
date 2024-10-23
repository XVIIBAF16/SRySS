## Objetivo
How about some hide and seek heh?Look at this image [here](https://artifacts.picoctf.net/c/237/atbash.jpg).
## Solución
En este reto nos dan una imagen para extraer basandonos en lo que dice el reto

Usamos el comando y cuando pida contraseña damos enter:
```
HideToSee % steghide extract -sf atbash.jpg 
krxlXGU{zgyzhs_xizxp_05y2z65z}
```

Nos da la flag enctriptada asi que nos vamos a cyberchaf y la des encriptamos en Atabash Cipher:
![HideToSee](/imagenes/HideToSee.png)

Y nos da la flag:
```
picoCTF{atbash_crack_05b2a65a}
```
## Notas adicionales
## Referencias