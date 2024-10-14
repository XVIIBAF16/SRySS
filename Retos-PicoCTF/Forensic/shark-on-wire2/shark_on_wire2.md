## Objetivo
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap). Recover the flag that was pilfered from the network.
## Solución

```
En este reto nos dan un archivo pca, verificamos el atchivo y buscamos cosas raras en el, biscamos el puerto 22 y vemos que se repite mucho:
```

![shark](/imagenes/sharkonwire.png)

```
Vemos que se reepite mucho los numeros, creamos un script en python para deccodificar la flag;
```

```
from scapy.all import *

packets = rdpcap('capture.pcap')

flag=''

for p in packets:
	if UDP in p and p[UDP].dport == 22:
		if p[UDP].sport > 5000:
			flag += chr(p[UDP].sport-5000)

print(flag)
```

```
ejecutamos
python3 flag
```

```
Y vemos la flag:
picoCTF{p1LLf3r3d_data_v1a_st3g0}
```
## Notas adicionales
## Referencias