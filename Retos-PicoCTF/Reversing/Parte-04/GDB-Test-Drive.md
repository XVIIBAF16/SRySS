## Objetivo
Can you get the flag?Download this [binary](https://artifacts.picoctf.net/c/85/gdbme).
## Solución
En este reto nos proporcionan un archivo que tenemos que ejecutar para que nos regrese la flag, en el mismo reto nos proporcionan los comandos a ejecutar asi que los ejecutamos:

```
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```

![GDB](/imagenes/GDB.jpeg)

![GDB 2](/imagenes/GDB(1).jpeg)

Flag:
```
picoCTF{d3bugg3r_dr1v3_197c378a}
```
## Notas adicionales
## Referencias