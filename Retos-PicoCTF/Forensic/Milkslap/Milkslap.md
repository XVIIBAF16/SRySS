## Objetivo
[🥛](http://mercury.picoctf.net:5013/)
## Solución


```
En este reto nos proporcionan una pagina web
```

![Milkslap](/imagenes/Milkslap.png)
```
Buscando por la pagina web no encontramos nada asi que decidi descargar el gif o imagen para analizarla mejor
```

![Milkslap 2](/imagenes/Milkslap(1).png)

```
Una vez en terminal vemos informacion dee la imagen:

% file concat_v.png 
concat_v.png: PNG image data, 1280 x 47520, 8-bit/color RGB, non-interlaced
```

```
Ejecutamos:

zsteg concat_v.png
imagedata           .. file: dBase III DBT, version number 0, next free block index 3368931841, 1st item "\001\001\001\001"
b1,b,lsb,xy         .. text: "picoCTF{imag3_m4n1pul4t10n_sl4p5}\n"
b1,bgr,lsb,xy       .. <wbStego size=9706075, data="\xB6\xAD\xB6}\xDB\xB2lR\x7F\xDF\x86\xB7c\xFC\xFF\xBF\x02Zr\x8E\xE2Z\x12\xD8q\xE5&MJ-X:\xB5\xBF\xF7\x7F\xDB\xDFI\bm\xDB\xDB\x80m\x00\x00\x00\xB6m\xDB\xDB\xB6\x00\x00\x00\xB6\xB6\x00m\xDB\x12\x12m\xDB\xDB\x00\x00\x00\x00\x00\xB6m\xDB\x00\xB6\x00\x00\x00\xDB\xB6mm\xDB\xB6\xB6\x00\x00\x00\x00\x00m\xDB", even=true, mix=true, controlbyte="[">
b2,r,lsb,xy         .. file: SoftQuad DESC or font file binary
b2,r,msb,xy         .. file: VISX image file
b2,g,lsb,xy         .. file: VISX image file
b2,g,msb,xy         .. file: SoftQuad DESC or font file binary - version 15722
b2,b,msb,xy         .. text: "UfUUUU@UUU"
b4,r,lsb,xy         .. text: "\"\"\"\"\"#4D"
b4,r,msb,xy         .. text: "wwww3333"
b4,g,lsb,xy         .. text: "wewwwwvUS"
b4,g,msb,xy         .. text: "\"\"\"\"DDDD"
b4,b,lsb,xy         .. text: "vdUeVwweDFw"
b4,b,msb,xy         .. text: "UUYYUUUUUUUU"
```

```
Y vemoss que la flag se enccuentra ahi
```

## Notas adicionales
## Referencias
