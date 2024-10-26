## Objetivo
Can you find the flag? [shark2.pcapng](https://mercury.picoctf.net/static/0fe13a33318e756f71c35cb490e64c81/shark2.pcapng).
## Solución
En este reto nos dan un archivo .pcapng para analizarlo asi que lo abrimos con WireShark

En wireeShark filtramos por tcp.stream eq 6 y revisamos los registros y encontramos que se descargo un archivo llamado flag.txt asi que seguimos su TCP Stream:
![Wireshark-twoo](/imagenes/Wireshark-twoo.png)

Y encontramos la flag pero al parecer esta encriptada:
![Wireshark-twoo 2](/imagenes/Wireshark-twoo(1).png)

Seguimos buscando y ahora filtramos por ip.addr == 18.217.1.57, encontramos otra flag pero tambien encriptada, seguimos buscando, nos damos cuenta que hay muchas flags encriptadas


hasta que encontramos la cadena:
```
cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==
```

La dessencriptamos en cyberchef:
![Wireshark-twoo 3](/imagenes/Wireshark-twoo(2).png)

Y nos da la flag:
```
picoCTF{dns_3xf1l_ftw_deadbeef}
```

## Notas adicionales
## Referencias