## Objetivo
How well can you perfom basic binary operations?Start searching for the flag here `nc titan.picoctf.net 52026`
## Solución

```
% nc titan.picoctf.net 52026

Welcome to the Binary Challenge!"
Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.

Binary Number 1: 10000101
Binary Number 2: 01010000


Question 1/6:
Operation 1: '>>'
Perform a right shift of Binary Number 2 by 1 bits .
Enter the binary result: 00101000
Correct!

Question 2/6:
Operation 2: '&'
Perform the operation on Binary Number 1&2.
Enter the binary result: 00000000
Correct!

Question 3/6:
Operation 3: '+'
Perform the operation on Binary Number 1&2.
Enter the binary result: 11010101
Correct!

Question 4/6:
Operation 4: '|'
Perform the operation on Binary Number 1&2.
Enter the binary result: 11010101
Correct!

Question 5/6:
Operation 5: '*'
Perform the operation on Binary Number 1&2.
Enter the binary result: 10100110010000
Correct!

Question 6/6:
Operation 6: '<<'
Perform a left shift of Binary Number 1 by 1 bits.
Enter the binary result: 100001010
Correct!

Enter the results of the last operation in hexadecimal: 0x10A

Correct answer!
The flag is: picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_6ab1ad84}
```
## Notas adicionales
## Referencias
