## Objetivo
Download this disk image, find the key and log into the remote machine.Note: if you are using the webshell, download and extract the disk image into`/tmp` not your home directory.

- [Download disk image](https://artifacts.picoctf.net/c/71/disk.img.gz)
- Remote machine: `ssh -i key_file -p 64886 ctf-player@saturn.picoctf.net`
## Solución

```
En este reto nos dan un archivo .img y un comando ssh para conectarnos con la maquina de forma remota, extrayendo la key o password del ussuario del archivo img asi que eejecutamos slos iguientees comandos:
```

```
Operation_Oni % mmls disk.img                
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000471039   0000264192   Linux (0x83)
```

```
En base a la info del comando ejecutamos el siguiente tomando en cuneta donde inicia la particion del archivo .img:
```

```
Operation_Oni % fls -o 0000206848 -r disk.img  
d/d 470:	root
+ r/r 2344:	.ash_history
+ d/d 3916:	.ssh
++ r/r 2345:	id_ed25519
++ r/r 2346:	id_ed25519.pub

solo mostre n eel writeeup lo que nos interesa
```

```
Operation_Oni % icat -o 0000206848 disk.img 2344
ssh-keygen -t ed25519
ls .ssh/
halt
```

```
vemos la llave privada con el comando:
```

```
Operation_Oni % icat -o 0000206848 disk.img 2345 > key_file
Operation_Oni % chmod 600 key_file
Operation_Oni % cat key_file 
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
```

```
Y nos conectamos a ssh:
Operation_Oni % ssh -i key_file -p 62923 ctf-player@saturn.picoctf.net
```

![Operation Oni](/imagenes/Operation_Oni.png)

## Notas adicionales
## Referencias