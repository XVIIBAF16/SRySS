
## Objetivo
Decode this [message](https://jupiter.challenges.picoctf.org/static/fc1edf07742e98a480c6aff7d2546107/message.wav) from the moon.
## Solución

```
En este reto nos dan un archivo .wav, abrimos con audacity y vemos que no enontramos nada importante, buscamos en internet STTV Deccoder y clonamos el primer repositorio que nos sale en la busqueda:

una vez clonado usamos la herramienta para decodificar el archivo:
```

```
% sstv -d message.wav -o flag.png
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 1
[sstv] Decoding image...                                   [####################################################################################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!

% ls
flag.png	m00nwalk.md	message.wav

% open flag.png 
```
```
Abrimos la imagen y podemos ver la flag
```

![STTV](/imagenes/flag.png)
## Notas adicionales
## Referencias
[SSTV Decoder](https://github.com/colaclanth/sstv)