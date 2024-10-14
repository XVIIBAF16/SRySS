## Objetivo

This is a really weird text file [TXT](https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt)? Can you find the flag?

## Solución

```
En este reto nos proporcionan lo que parece ser un archivo txt, al ver su contenido vemos que hay simbolos y caracterees extraños:`

`Nos vamos a terminal y ejecutamos los comandos:

% file flag.txt flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced

y vemos que en realidad es una imagen png asi que cambiamos su extension:

% mv flag.txt flag.png
```

![extensions](/imagenes/extensions.png)

```
y vemos la imagen:
```

![extensions 2](/imagenes/extensions(2).png)
## Notas adicionales

## Referencias