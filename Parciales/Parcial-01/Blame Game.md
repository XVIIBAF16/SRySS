## Objetivo
Someone's commits seems to be preventing the program from working. Who is it?You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/73/challenge.zip)
## Solución

```
% cd drop-in2
fabianmartinezalonso@MacBook-Pro-de-Fabian drop-in2 % cat message.py 
print("Hello, World!"
% git log -- *.py                                    
commit fadeca9476b6713ec8cdda633aca9e9aebffc698
Author: picoCTF{@sk_th3_1nt3rn_e9957ce1} <ops@picoctf.com>
Date:   Sat Mar 9 21:09:11 2024 +0000

    optimize file size of prod code

commit 2dd46769e2d65656bb14aed0ff5d3237daaa7d9d
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:11 2024 +0000

    create top secret project
```
## Notas adicionales
## Referencias
