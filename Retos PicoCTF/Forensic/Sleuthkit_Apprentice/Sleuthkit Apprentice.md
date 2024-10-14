## Objetivo
Download this disk image and find the flag.Note: if you are using the webshell, download and extract the disk image into`/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/138/disk.flag.img.gz)
## Solución

```
En este reto nos dan un archivo .img asi que elo analizaremos con los siguientes comandos:
```

```
Sleuthkit_Apprentice % mmls disk.flag.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)
```

```
Con la informacion del comando vemos la ultima particion donde generalmente es donde se encuentra la flag:
```

```
Sleuthkit_Apprentice % fls -o 0000360448 -r disk.flag.img 
d/d 1995:	root
+ r/r 2363:	.ash_history
+ d/d 3981:	my_folder
++ r/r * 2082(realloc):	flag.txt
++ r/r 2371:	flag.uni.txt


Se muestra en el writeup solo lo que nos interesa, vemos qu ehay varios archivos llamados flag asi que los vemoss con icat:
```

```
Sleuthkit_Apprentice % icat -o 0000360448 disk.flag.img 2082
            3.449677            13.056403

vemos que no hay mada interesante aqui asi que vemos el otro archivo:
```

```
Sleuthkit_Apprentice % icat -o 0000360448 disk.flag.img 2371
picoCTF{by73_5urf3r_2f22df38}

Y encontramos la flag
```
## Notas adicionales
## Referencias