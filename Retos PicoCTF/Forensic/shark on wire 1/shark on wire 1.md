## Objetivo
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap). Recover the flag.
## Solución

```
En este reto nos dan una archivo con una extensión .pcap
Lo abrimos con Wireshark para ver su contenido:
```

![shark](/imagenes/shark.png)

```
Nos vamos al buscador y ponemos:
	`udp.stream eq 1`
```

![shark 2](/imagenes/shark(2).png)

```
Elegimos el primero y damos click derecho -> follow -> UDP stream
```

![shark 3](/imagenes/shark(3).png)

```
Una vez elegida la opcion en la siguiente ventana ponemos el valor 6 en stream abajo a la derecha y obtendremos la flag:
```

![shark 4](/imagenes/shark(4).png)
## Notas adicionales
## Referencias
[shark on wire 1](https://github.com/kevinjycui/picoCTF-2019-writeup/blob/master/Forensics/shark%20on%20wire%201/README.md)