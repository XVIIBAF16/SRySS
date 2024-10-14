## Objetivo
Download this disk image and find the flag.Note: if you are using the webshell, download and extract the disk image into`/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/213/disk.flag.img.gz)
## Solución

```
En este reto nos dan un archivo .img el ccual analizaremos para encontrar la flag con los siguientees comandos:
```

```
Operation_Orchid % mmls disk.flag.img 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000411647   0000204800   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000411648   0000819199   0000407552   Linux (0x83)
```

```
En base a la info del comando vemos la particion del disco con el comando:
```

```
Operation_Orchid % fls -o 0000411648 -r disk.flag.img
d/d 472:	root
+ r/r 1875:	.ash_history
+ r/r * 1876(realloc):	flag.txt
+ r/r 1782:	flag.txt.enc
```

```
Operation_Orchid % fls -o 0000411648 disk.flag.img 472
r/r 1875:	.ash_history
r/r * 1876(realloc):	flag.txt
r/r 1782:	flag.txt.enc
```

```
Vemos lo que hizo el usuario en el archivo flag.txt y vemos que ejecuto varios comandos:

Operation_Orchid % icat -o 0000411648 disk.flag.img 1875               
touch flag.txt
nano flag.txt 
apk get nano
apk --help
apk add nano
nano flag.txt 
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
```

```
Asi que mandamos la flag encriptada a un archivo:

Operation_Orchid % icat -o 0000411648 disk.flag.img 1782 > flag.txt.enc
```

```
Desencriptamos la flag usando el mismo comando que uso para encriptarla pero ahora le ponemos el parametro -d para desencriptar y cambiamos el archivo de entrada a flag.txt.enc y de salida a flag.txt de la siguiente manera:

Operation_Orchid % openssl aes256 -salt -d -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567  
```

```
Vemos el conetnido de flag.txt y nos encontramos con la bandera dessencriptada:

Operation_Orchid % cat flag.txt
picoCTF{h4un71ng_p457_5113beab}
```
## Notas adicionales
## Referencias