## Objetivo
Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](https://mercury.picoctf.net/static/626ea9c275fbd02dd3451b81f9c5e249/dds1-alpine.flag.img.gz)
## Solución

```
En este reto nos proporcionan un archivo .img.gz, viendo la descripcion del reto nos damos cuenta que teenemos que buscar en los strings del archivo asi que usamos el comando strings y grep para encontrar la flag:
```

```
% strings dds1-alpine.flag.img | grep picoCTF
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_a6f4cab5}
```
## Notas adicionales
## Referencias
