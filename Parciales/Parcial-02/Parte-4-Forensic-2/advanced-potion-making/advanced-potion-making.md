## Objetivo
Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it!

| CHALLENGE ENDPOINTS             |                                                                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Download advanced-potion-making | [advanced-potion-making](https://artifacts.picoctf.net/picoMini+by+redpwn/Forensics/advanced-potion-making/advanced-potion-making) |
## Solución
En este reto nos dan un archivo para analizar, primero checamos el archivo con xxd:
```
advanced-potion-making % xxd advanced-potion-making 
00000000: 8950 4211 0d0a 1a0a 0012 1314 4948 4452  .PB.........IHDR
00000010: 0000 0990 0000 04d8 0802 0000 0004 2de7  ..............-.
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
```


Cambiamos el nombre del archivo a un .png:
```
advanced-potion-making % mv advanced-potion-making flag.png
```

Y vemos que al principio la extension que tiene no es del todo entendible, la cambiamos por .PNG con eel comando hexedit:
![advanced-potion-making](/imagenes/advanced-potion-making.png)


Abrimos la imagen con java ya que la imagen solo muestra el color rojo y dentro de steegsolve nos movemos con las flechas hasta encontrar algo:
```
advanced-potion-making % java -jar /opt/bin/stegsolve.jar 
```

Y encontramos la imagen que contiene la flag:
![advanced-potion-making 2](/imagenes/advanced-potion-making(1).png)

Flag:
```
picoCTF{w1z4rdry}
```
## Notas adicionales
## Referencias