## Objetivo
This program has constructed the flag using hex ascii values. Identify the flag text by disassembling the program.
You can download the file from [here](https://artifacts.picoctf.net/c/506/asciiftw).
## Solución
En este reto nos dan una archivo ELF, asi que ejecutamos gdb para ver el contenido:
```
gdb ./asciiftw
GNU gdb (GDB) 15.2
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-apple-darwin22.6.0".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./asciiftw...
(No debugging symbols found in ./asciiftw)
```

Y ejecutamos layout text:
```
(gdb) layout next
```

![ASCII-FTW](/imagenes/ASCII-FTW.png)

Nos muestra una serie de binarios, tratamos de veer que significa cada uno y descubrimos que las primeras tres letras son pic, entonces suponemos que esta es la flag asi que lo extraemos

```
0x70,-0x30 (%rbp)
0x69,-0x2f (%rbp)
0x63,-0x2e (%rbp)
0x6f,-0x2d (%rbp)
0x43,-0x2c (%rbp)
0x54,-0x2b (%rbp)
0x46,-0x2a (%rbp)
0x7b,-0x29 (%rbp)
0x41,-0x28 (%rbp)
0x53,-0x27 (%rbp)
0x43,-0x26 (%rbp)
0x49,-0x25 (%rbp)
0x49,-0x24 (%rbp)
0x5f,-0x23 (%rbp)
0x49,-0x22 (%rbp) 
0x53,-0x21 (%rbp)  
0x5f,-0x20 (%rbp)  
0x45,-0x1f (%rbp)   
0x41,-0x1e (%rbp)  
0x53,-0x1d (%rbp)   
0x59,-0x1c (%rbp)   
0x5f,-0x1b (%rbp)  
0x33,-0x1a (%rbp)   
0x43,-0x19 (%rbp)   
0x46,-0x18 (%rbp)   
0x34,-0x17 (%rbp)   
0x42,-0x16 (%rbp)   
0x46,-0x15 (%rbp)   
0x41,-0x14 (%rbp)  
0x44,-0x13 (%rbp)   
0x7d,-0x12 (%rbp)   
_ax30 (%rbp),%eax
```


Traduciendo o descifrando todo nos da la flag:
```
picoCTF{ASCII_IS_EASY_3CF4BFAD}
```
## Notas adicionales
## Referencias