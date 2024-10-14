## Objetivo

I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/2e739f9e0dc9f4c1556ea6b033c3ec8e/Forensics%20is%20fun.pptm)
## Solución

```
En este reto nos dan una archivo con extension .pptm, guiandonos por el nombre del reto nos damos cuenta que se trata de las Macros en el archiv asi que ejecutaremoss los siguientes comandos: 
```

```
% binwalk Forensics\ is\ fun.pptm 
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, compressed size: 674, uncompressed size: 10660, name: [Content_Types].xml
1243          0x4DB           Zip archive data, at least v2.0 to extract, compressed size: 259, uncompressed size: 738, name: _rels/.rels
2063          0x80F           Zip archive data, at least v2.0 to extract, compressed size: 951, uncompressed size: 5197, name: ppt/presentation.xml
3064          0xBF8           Zip archive data, at least v2.0 to extract, compressed size: 189, uncompressed size: 311, name: ppt/slides/_rels/slide46.xml.rels
```

```
% 7z x Forensics\ is\ fun.pptm 

7-Zip [64] 17.05 : Copyright (c) 1999-2021 Igor Pavlov : 2017-08-28
p7zip Version 17.05 (locale=utf8,Utf16=on,HugeFiles=on,64 bits,8 CPUs x64)

Scanning the drive for archives:
1 file, 100093 bytes (98 KiB)

Extracting archive: Forensics is fun.pptm
--
Path = Forensics is fun.pptm
Type = zip
Physical Size = 100093

Everything is Ok

Files: 153
Size:       237329
Compressed: 100093
```

```
Veremos una serie de archivos que nos da el archivo descomprimido asi que verificamos algunos archivos
```

```
% ls -la
-rw-r--r--@  1   staff  100093 10 oct 18:40 Forensics is fun.pptm
-rw-r--r--@  1   staff       0 10 oct 18:45 
-rw-r--r--   1   staff   10660  1 ene  1980 [Content_Types].xml
drwx------   3   staff      96 10 oct 18:49 _rels
drwx------   5   staff     160 10 oct 18:49 docProps
drwx------  12   staff     384 10 oct 18:49 ppt100093 10 oct 18:40 Forensics is fun.pptm
```

```
% cat ppt/slideMasters/hidden 
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q% 
```

```
Encontramos esto que al parecer esto esta encriptado en base64 asi que lo desencriptamos aquitanod espacios y agregando == para que lo interprete como base64 y veremos que ahi esta la flag
```

```
echo ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ== | base64 -d
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}%   
```
## Notas adicionales
## Referencias