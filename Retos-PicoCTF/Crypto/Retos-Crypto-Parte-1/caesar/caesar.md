## Objetivo

Decrypt this [message](https://jupiter.challenges.picoctf.org/static/49f31c8f17817dc2d367428c9e5ab0bc/ciphertext).
## Solución

```
En este reto nos proporcionan un archivo, asi que en terminal vemos lo que contiene este archivo:
```

```
caesar % ls
ciphertext
caesar % cat ciphertext 
picoCTF{ynkooejcpdanqxeykjrbdofgkq}
```

```
Al parecer no esta dando una flag encriptada, basandonos en el nombre del reto nos damos cuenta que esta cifrado en fomrato Cesar asi que nos vamos a la pagina
https://www.dcode.fr/cifrado-cesar para poder desenciptar la flag
```

![caesar](/imagenes/caesar.png)

```
Nos da varias opciones y elegimos la opción mas coherente o entendible y vemos que si es la flag

picoCTF{crossingtherubiconvfhsjkou}
```
## Notas adicionales
## Referencias
[dcode](https://www.dcode.fr/cifrado-cesar)