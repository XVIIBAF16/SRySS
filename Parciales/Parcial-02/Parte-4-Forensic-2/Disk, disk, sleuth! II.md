## Objetivo
All we know is the file with the flag is named `down-at-the-bottom.txt`... 
Disk image: [dds2-alpine.flag.img.gz](https://mercury.picoctf.net/static/544be9762e9f9c0adcbeb7bcf27f49a2/dds2-alpine.flag.img.gz)
## Solución
En este reto nos dan un archivo .img para analizar

ejecutando los comandos:
```
mmls dds2-alpine.flag.img                 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Linux (0x83)
```

```
fsstat -o 2048 dds2-alpine.flag.img | head    
FILE SYSTEM INFORMATION
--------------------------------------------
File System Type: Ext3
Volume Name: 
Volume ID: dc53a3bb0ae739a5164c89db56bbb12f

Last Written at: 2021-02-16 12:21:20 (CST)
Last Checked at: 2021-02-16 12:21:19 (CST)

Last Mounted at: 2021-02-16 12:21:19 (CST)
```

```
fls -r -o 2048 dds2-alpine.flag.img | grep down   
++ d/d 2177:	if-down.d
++ d/d 2178:	if-post-down.d
++ d/d 2180:	if-pre-down.d
++ d/d 2204:	shutdown
+ r/r 18291:	down-at-the-bottom.txt
+ l/l 18311:	ifdown
+ r/r 18344:	openrc-shutdown
+++++ r/r 12472:	down.sh
fabianmartinezalonso@MacBook-Pro-de
```

```
icat -o 2048 ./dds2-alpine.flag.img 18291
```

Y nos muestra la flag:
```
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( p ) ( i ) ( c ) ( o ) ( C ) ( T ) ( F ) ( { ) ( f ) ( 0 ) ( r ) ( 3 ) ( n )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( s ) ( 1 ) ( c ) ( 4 ) ( t ) ( 0 ) ( r ) ( _ ) ( n ) ( 0 ) ( v ) ( 1 ) ( c )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
   _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( 3 ) ( _ ) ( 6 ) ( 9 ) ( a ) ( b ) ( 1 ) ( d ) ( c ) ( 8 ) ( } )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
```


Flag:
```
picoCTF{f0r3ns1c4t0r_n0v1c3_69ab1dc8}
```
## Notas adicionales
## Referencias