## Objetivo
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/picopico.key). Recover the flag.
## Solución

```
En este rto al igual que el anterior con este nombre nos dan un archivo .pcap y una rchivo .key, aplicamos los mismos comandos para ver su salida
```

```
A comparacion del anteerior este mustra mas infomracion asi que aplicamos un grep
```

```
% ssldump -r capture.pcap -k picopico.key -d | grep picoCTF
Short read: -1295 bytes available (expecting 2)
Short read: -1295 bytes available (expecting 2)
Short read: -1295 bytes available (expecting 2)
Short read: -1295 bytes available (expecting 2)
    61 67 3a 20 70 69 63 6f 43 54 46 7b 74 68 69 73    ag: picoCTF{this
    67 3a 20 70 69 63 6f 43 54 46 7b 74 68 69 73 2e    g: picoCTF{this.
    Pico-Flag: picoCTF{this.is.not.your.flag.anymore}
    00 00 00 01 00 00 00 01 70 69 63 6f 43 54 46 7b    ........picoCTF{
```

```
Nos muestra una flag pero metiendola en la pagina vemos que es una flag falsa asi que seguimos buscando, para hacerlo mas facil mandamos la salida a un archiv, een mi caso llamado flag
```

```
% ssldump -r capture.pcap -k picopico.key -d > flag         
Short read: -1295 bytes available (expecting 2)
Short read: -1295 bytes available (expecting 2)
Short read: -1295 bytes available (expecting 2)
Short read: -1295 bytes available (expecting 2)
```

```
Al parecer por comandos nos sigue moestrando la misma flag asi que buscamos por medio de un editor de texto
```

```
Y vemos que hay muchas salidas con la bandera falsa pero siguiendo filtrando por picoCTF nos muestra la verdadera flag:
```

![WebNet1](/imagenes/WeebNet1.png)

```
picoCTF{honey.roasted.peanuts}
```

## Notas adicionales
## Referencias