## Objetivo
Now you DON’T see me.This [report](https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?
## Solución
En este reto nos dan un PDF para a analizarlo, al abrirlo nos damos cuenta que la flag y otras partes del texto estan censuradas asi que ejecutamos el comando:
```
Redaction-gone-wrong % pdftotext Financial_Report_for_ABC_Labs.pdf
```

Nos da un archivo con el mismo nombre pero extension .txt, le hacemos un cat y un grep:
```
% cat Financial_Report_for_ABC_Labs.txt | grep picoCTF
picoCTF{C4n_Y0u_S33_m3_fully}
```

Y nos da la flag:
```
picoCTF{C4n_Y0u_S33_m3_fully}
```
## Notas adicionales
## Referencias