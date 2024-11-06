## Objetivo
What does asm3(0xba6c5a02,0xd101e3dd,0xbb86a173) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://jupiter.challenges.picoctf.org/static/cb753ae52bca4aa303deca5fbfb01bfb/test.S)
## Solución
En este reto nos dan un archivo .S en ensamblador con el contenido:

```
asm3:
	<+0>: push ebp
	<+1>: mov ebp,esp
	<+3>: xor eax,eax
	<+5>: mov ah,BYTE PTR [ebp+0xb]
	<+8>: shl ax,0x10
	<+12>: sub al,BYTE PTR [ebp+0xd]
	<+15>: add ah,BYTE PTR [ebp+0xc]
	<+18>: xor ax,WORD PTR [ebp+0x12]
	<+22>: nop
	<+23>: pop ebp
	<+24>: ret
```

Al analizarlo vemos que esta haciendo una serie de operaciones aritmeticas a los valores que le pasamos, asi que creamos una serie de scripts que hagan el procedimiento para que nos de la respuesta:  

Script 1: test_modi.S:
```
.intel_syntax noprefix
.global asm3

asm3:
    push    ebp
    mov     ebp, esp
    xor     eax, eax
    mov     ah, BYTE PTR [ebp + 0xb]
    shl     ax, 0x10
    sub     al, BYTE PTR [ebp + 0xd]
    add     ah, BYTE PTR [ebp + 0xc]
    xor     ax, WORD PTR [ebp + 0x12]
    nop
    pop     ebp
    ret
```

Script 2: solve.c
```
 #include <stdio.h>

 int asm3(int, int, int);

 int main(int argc, char* argv[])
 {
     printf("0x%x\n", asm3(0xba6c5a02,0xd101e3dd,0xbb86a173));
     return 0;
 }
```

Y ya con los archivos creados ejecutamos los siguientes comandos:
```
gcc -masm=intel -m32 -c test_modi.S -o test_modi.o
gcc -m32 -c solve.c -o solve.o
gcc -m32 test_modi.o solve.o -o solve
```

Y ejecutamos el ultimo archivo: dandonos la flag
```
$ ./solve
0x669b
```

flag sin fomrato:
```
0x669b
```

## Notas adicionales
## Referencias