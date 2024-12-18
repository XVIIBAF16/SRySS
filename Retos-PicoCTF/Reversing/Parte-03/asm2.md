## Objetivo
What does asm2(0x4,0x2d) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://jupiter.challenges.picoctf.org/static/ceac75672637589213b952abe32c84b3/test.S)
## Solución
En este reto nos dan un archivo .S con código ensamblador con el codigo:

```
asm2:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0xd1
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x5fa1
	<+38>:	jle    0x501 <asm2+20>
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]
	<+43>:	leave  
	<+44>:	ret
```

Analizando vemos que realiza varias operaciones, asi que revisando y haciendo las operaciones del código paso a paso:
- La función toma dos argumentos: el primero (`0x4`) y el segundo (`0x2d`).
- Luego, incrementa el segundo argumento (almacenado en `[ebp-0x4]`) en 1 en cada iteración, mientras que el primer argumento (almacenado en `[ebp-0x8]`) se incrementa en `0xd1` (209).
- El bucle continúa hasta que el primer argumento supera `0x5fa1` (24353).


Y nos da el resultado, que es la flag (Sin formato):
```
0xa3
```
## Notas adicionales
## Referencias