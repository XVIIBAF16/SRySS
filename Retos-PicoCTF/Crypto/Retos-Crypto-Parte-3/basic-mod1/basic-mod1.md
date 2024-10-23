## Objetivo
We found this weird message being passed around on the servers, we think we have a working decryption scheme.Download the message [here](https://artifacts.picoctf.net/c/128/message.txt).Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)
## Solución
En este reto nos dan un archivo llamado message.txt con valores numericos

Usaremos el script een python:
```
def decode(number):
    r = number % 37
    return r

def main():
    f = open("message.txt", "r", encoding="UTF-8")
    lst = f.read().split()
    # print(lst[0])

    dec_lst = []

    for i in range(len(lst)):
        dec_lst.append(decode(int(lst[i])))

    abc="abcdefghijklmnopqrstuvwxyz0123456789_"
    print(len(abc))
    print(dec_lst)
    for letter in dec_lst:
        print(abc[letter],end="")

if __name__ == '__main__':
    main()
```

Y al ejecutarlo nos dara la flag desencriptada:
![basic-mod1](/imagenes/basic-mod1.png)

Y la flag es:
```
picoCTF{r0und_n_r0und_b6b25531}
```
## Notas adicionales
## Referencias