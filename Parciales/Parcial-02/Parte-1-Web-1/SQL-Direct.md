## Objetivo
Connect to this PostgreSQL server and find the flag!`psql -h saturn.picoctf.net -p 61436 -U postgres pico`Password is `postgres`
## Solución
En este reto nos proporcionan un comando para conectarnos por medio de postgres usando la contraseña postgres:

Investigando un poco deel lenguaje que usa encontramos el comando:
```
\dt
```
para listar las tablas publicas:
![SQL-Direct](/imagenes/SQL-Direct.png)

Viendo la info que nos da el comando encontramos que hay una tabla llamada flags asi que la consultamos para ver su contenido:
![SQL-Direct 2](/imagenes/SQL-Direct(1).png)

Y encontramos la flag:
```
picoCTF{L3arN_S0m3_5qL_t0d4Y_21c94904}
```
## Notas adicionales
## Referencias