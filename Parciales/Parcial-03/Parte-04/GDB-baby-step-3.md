## Objetivo
Now for something a little different. `0x2262c96b` is loaded into memory in the`main` function. Examine byte-wise the memory that the constant is loaded in by using the GDB command `x/4xb addr`. The flag is the four bytes as they are stored in memory. If you find the bytes `0x11 0x22 0x33 0x44` in the memory location, your flag would be: `picoCTF{0x11223344}`.
Debug [this](https://artifacts.picoctf.net/c/531/debugger0_c).
## Solución
En este reto nos dan un archivo ELF, asi que seguimos el mismo procedimiento:
```
gdb debugger0_c 
```

Una vez dentro ejecutamos:
```
(gdb) set disassembly-flavor intel
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
0x0000000000401106  main
0x0000000000401130  __libc_csu_init
0x00000000004011a0  __libc_csu_fini
0x00000000004011a8  _fini

(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:	endbr64
   0x000000000040110a <+4>:	push   rbp
   0x000000000040110b <+5>:	mov    rbp,rsp
   0x000000000040110e <+8>:	mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:	mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:	mov    DWORD PTR [rbp-0x4],0x2262c96b
   0x000000000040111c <+22>:	mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040111f <+25>:	pop    rbp
   0x0000000000401120 <+26>:	ret
End of assembler dump.


(gdb) break main
Breakpoint 1 at 0x40110e
```

```
(gdb) layout asm
```

![GDB3](/imagenes/GDB3.png)

```
(gdb) break *0x40111f
(gdb) c
Continuing
(gdb) info registers eax
(gdb) x/4xb $rbp-4
0x7fffffff: 0x6b 0xc9 0x62 0x22
```

Y esto nos da la flag:
```
**picoCTF{0x6bc96222}**
```

## Notas adicionales
## Referencias