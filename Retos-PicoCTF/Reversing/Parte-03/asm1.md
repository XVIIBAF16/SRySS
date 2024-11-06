## Objetivo
What does asm1(0x2e0) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://jupiter.challenges.picoctf.org/static/f1c2358ff7d1e9386e41552c549cf2f6/test.S)
## Solución
En este reto al nos proporcionan un archivo .S que contiene código en ensamblador donde al parecer esta aplicando operaciones aritmética:

```
asm1:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x3fb
	<+10>:	jg     0x512 <asm1+37>
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x280
	<+19>:	jne    0x50a <asm1+29>
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0xa
	<+27>:	jmp    0x529 <asm1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0xa
	<+35>:	jmp    0x529 <asm1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0x559
	<+44>:	jne    0x523 <asm1+54>
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]
	<+49>:	sub    eax,0xa
	<+52>:	jmp    0x529 <asm1+60>
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0xa
	<+60>:	pop    ebp
	<+61>:	ret 
```

Asi que siguiendo el código y haciendo las operaciones aritméticas paso por paso:
- **Entrada:** `0x2e0` (736 en decimal).
- **Primera comparación:** `0x2e0 < 0x3fb` (1019) → No se salta.
- **Segunda comparación:** `0x2e0 > 0x280` (640) → Salta a restar.
- **Resta 10:** 0x2e0−0xa=0x2d60x2e0−0xa=0x2d6
- **Salida:** La función retorna `0x2d6`.


Vemos que la flag es, tal cual sin formato:
```
0x2d6
```
## Notas adicionales
## Referencias