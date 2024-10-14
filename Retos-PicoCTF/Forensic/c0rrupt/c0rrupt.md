## Objetivo
We found this [file](https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery). Recover the flag.
## Solución

```
En este reto nos dan un archivo al parcer corrupto, para este caso corregiremos el archivo para poder ver su contenido o sea la flag
```

```
Primero creamos una copia del arcchivo para trabajar sobre ese
% cp mystery flag.png

Corregimos los primeross 8 bytes para poder cambiar su extenison:
printf '\x89\x50\x4E\x47\x0D\x0A\x1A\x0A' | dd of=fixed.png bs=1 seek=0 count=8 conv=notrunc

Al parecer se cambio pero deja sin abrir
% xxd -g 1 fixed.png | head
00000000: 89 50 4e 47 0d 0a 1a 0a                          .PNG....


Corregimos otra vez 4 bytes
% printf '\x00\x00\x00\x0D\x49\x48\x44\x52' | dd of=fixed.png bs=1 seek=8 count=8 conv=notrunc


% xxd -g 1 fixed.png | head                                                                   
00000000: 89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52  .PNG........IHDR


corregimos errores:
% printf 'IDAT' | dd of=fixed.png bs=1 seek=87 count=4 conv=notrunc


printf '\x00\x00' | dd of=fixed.png bs=1 seek=83 count=2 conv=notrunc

Abrimos la imagen:
% open flag.png

```

```
Y vemos la bandera:
picoCTF{c0rrupt10n_1847995}
```

## Notas adicionales
## Referencias