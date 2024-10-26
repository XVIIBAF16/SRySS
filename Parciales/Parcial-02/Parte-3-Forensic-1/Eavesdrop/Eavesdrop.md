## Objetivo
Download this packet capture and find the flag.

- [Download packet capture](https://artifacts.picoctf.net/c/134/capture.flag.pcap)
## Solución
En este reto nos dan un .pcap para analizar, asi que lo vemos en WireShark, al analizarlo un rato encontramos una conversacion:
![Eavesdrop](/imagenes/Eavesdrop.png)


Vemos que hay un comando y un archivo del cual estan hablando, al final enontre un _salt_, lo converti a hexadecimal y lo guarde en un archivo llamado file.des3 y ejecute el comando del cual estaban halando:
![Eavesdrop 2](/imagenes/Eavesdrop(1).png)


Y en la terminal lo ejecutamos y nos da la flag:
```
Eavesdrop % openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.


Eavesdrop % cat file.txt
picoCTF{nc_73115_411_dd54ab67}
```
## Notas adicionales
## Referencias