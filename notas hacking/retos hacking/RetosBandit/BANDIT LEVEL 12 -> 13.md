## Objetivo
The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)
## Datos  acceso al nivel
```
Username: bandit12
Password: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```
## Solución

![RetoBandit12](Bandit12(1).png)

![RetoBandit12](Bandit12(2).png)
## Notas adicionales

```
Algunos tipos de compresion en Linux
-----------------------------------------------------
ext comp desc ver en consola
-----------------------------------------------------
.gz gzip gzip -d (gunzip) zcat
.bz2 bzip2 bzip2 -d (bunzip2) bzcat
.tar tar tar xf tar xO
----------------------------------------------------
otros (instalar) :
.zip zip unzip (7z x)
.rar rar unrar (7z x)
```
## Referencias
