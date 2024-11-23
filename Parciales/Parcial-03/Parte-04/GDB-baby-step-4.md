## Objetivo
`main` calls a function that multiplies `eax` by a constant. The flag for this challenge is that constant in decimal base. If the constant you find is 0x1000, the flag will be `picoCTF{4096}`.
Debug [this](https://artifacts.picoctf.net/c/532/debugger0_d).
## Solución
En este reto nos dan un archivo ELF como en los retos anteriores asi que seguimos los mismos comandos a ejecutar:
```
gdb debugger0_d
```

Una vez dentro ejecutamos:
```
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401020  _start
0x0000000000401050  _dl_relocate_static_pie
0x0000000000401060  deregister_tm_clones
0x0000000000401090  register_tm_clones
0x00000000004010d0  __do_global_dtors_aux
0x0000000000401100  frame_dummy
0x0000000000401106  func1
0x000000000040111c  main
0x0000000000401150  __libc_csu_init
0x00000000004011c0  __libc_csu_fini
0x00000000004011c8  _fini


(gdb) set disassembly-flavor intel
(gdb) break main
Breakpoint 1 at 0x401124
```

```
(gdb) layout asm
```

Y nos muestra:
![GDB4](/imagenes/GDB4.png)

Una vez aqui ejecutamos:
```
(gdb) run
(gdb) ni
(gdb) si
(gdb) print/d 0x3269
$1 = 12905
```

Y esto nos da el resultado de la flag:
```
picoCTF{12905}
```
## Notas adicionales
## Referencias