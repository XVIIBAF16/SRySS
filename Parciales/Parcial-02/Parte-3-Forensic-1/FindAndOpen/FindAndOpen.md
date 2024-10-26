## Objetivo
Someone might have hidden the password in the trace file.Find the key to unlock [this file](https://artifacts.picoctf.net/c/496/flag.zip). [This tracefile](https://artifacts.picoctf.net/c/496/dump.pcap) might be good to analyze.
## Solución
En este reto nos dan un .zip y un archivo pcap que tenemoss que analizar para la contraseña del zip:

Analizamos el pcap y filtramos por !mdns:
![FindAndOpen](/imagenes/FindAndOpen.png)


Y seguimos el TCP stream y encontramos:
```
Flying on Ethernet secret: Is this the flag
iBwaWNvQ1RGe1Could the flag have been splitted?
PBwaWUvQ1RGe1Maybe try checking the other file
AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=
```


Desencriptanto encontramos que la contraseña es picoCTF{R34DING_LOKd_


asi que descomprimimos el archivo:
```
% unzip -P picoCTF{R34DING_LOKd_ flag.zip
Archive:  flag.zip
 extracting: flag                    
```


y nos da un archivo llamado flag que contiene la contraseña:
```
picoCTF{R34DING_LOKd_fil56_succ3ss_5ed3a878}
```
## Notas adicionales
## Referencias