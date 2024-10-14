## Objetivo
Find the flag in this [picture](https://jupiter.challenges.picoctf.org/static/916b07b4c87062c165ace1d3d31ef655/pico_img.png).
## Solución

```
En este reto nos proporccionan una imagen para analizar:
```

```
En terminal ejecutamos el comando:
	strings pico_img.png

Y al final de la salida nos dara la flag:
```


![Meta](/imagenes/Meta.png)


```
Otro metodo para encontrarla mas faicil sseria usando grep
	% strings pico_img.png | grep "picoCTF{"
	picoCTF{s0_m3ta_d8944929}K
```
## Notas adicionales
## Referencias
