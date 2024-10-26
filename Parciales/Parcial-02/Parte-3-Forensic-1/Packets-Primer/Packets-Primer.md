## Objetivo
Download the packet capture file and use packet analysis software to find the flag.

- [Download packet capture](https://artifacts.picoctf.net/c/195/network-dump.flag.pcap)
## Solución
En este reto nos proporcionan un archivo .pcap asi que lo analizamos con WireShark, al analizarlo nos damos cuenta que hay algo raro en uno de los registros asi que damos click derecho y seguir, TCP Stream:
![Packets-Primer](/imagenes/Packets-Primer.png)

Y nos muestra la flag:
![Packets-Primer 2](/imagenes/Packets-Primer(1).png)

```
picoCTF{p4ck37_5h4rk_b9d53765}
```
## Notas adicionales
## Referencias