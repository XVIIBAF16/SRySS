## Objetivo
The name of the game is [speed](https://www.youtube.com/watch?v=8piqd2BWeGI). Are you quick enough to solve this problem and keep it above 50 mph? [need-for-speed](https://jupiter.challenges.picoctf.org/static/cd51b2c95be9f3626db6fe6665afb5a3/need-for-speed).
## Solución
En este reto nos dan un archivo para ejecutar, asi que ejecutamos los comandos:

Comando 1, Otorgando permisos de ejecución al archivo:
```
chmod +x need-for-speed
```

Comando 2, Ejecutamos con gdb:
```
gdb need-for-speed
```

![NFS 3](/imagenes/NFS.jpeg)

Comando 3:
```
handle SIGALRM ignore
```

![NFS 3](/imagenes/NFS(1).jpeg)

Comando 4, Corremos el programa:
```
r
```

![NFS 4](/imagenes/NFS(3).jpeg)



Flag:
```
PICOCTF{Good job keeping bus #24c43740 speeding along!}
```
## Notas adicionales
## Referencias