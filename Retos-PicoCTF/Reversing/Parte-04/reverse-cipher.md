## Objetivo
We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/48babf8f8c4c6b8baf336680ea5b9ddf/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/48babf8f8c4c6b8baf336680ea5b9ddf/rev_this). Can you reverse the flag.
## Solución
En este reto nos dan dos archivos, uno de ellos tiene la flag encriptada, asi que hacemos reversing para que nos regrese la flag, asi que creamos un script:

script.py:
```
import os
import mmap

def memory_map(filename, access=mmap.ACCESS_READ):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDONLY)
    return mmap.mmap(fd, size, access=access)

with memory_map("rev_this") as bin_file:
    for i in range(8):
        print(chr(bin_file[i]), end = '')
    for i in range(8, 23):
        if (i & 1) == 0:
            print(chr(bin_file[i] - 5), end = '')
        else:
            print(chr(bin_file[i] + 2), end = '')
    print (chr(bin_file[23]))
```

![reverse cipher](/imagenes/reverse.jpeg)

Y lo ejecutamos:
```
python script.py
```

![reverse cchiper 2](/imagenes/reverse(1).jpeg)


Y nos da la flag:
```
picoCTF{r3v3rs312528e05}
```
## Notas adicionales
## Referencias
[reverse-cipher](https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/reverse_cipher.md)
