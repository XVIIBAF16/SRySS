## Objetivo
You will find the flag after decrypting this file
Download the encrypted flag [here](https://artifacts.picoctf.net/c/387/encrypted.txt).
## Solución
En este reto nos dan un archivo .txt con la flag cifrada:

```
cat encrypted.txt 
xqkwKBN{z0bib1wv_l3kzgxb3l_949in1i1}
```

Vemos que esta cifrada en rot13 asi que usamos cyberchef rot13 brute force:
![rot13](/imagenes/rot13.png)

Buscamos la flag

Flag:
```
picoCTF{r0tat1on_d3crypt3d_949af1a1}
```
## Notas adicionales
## Referencias