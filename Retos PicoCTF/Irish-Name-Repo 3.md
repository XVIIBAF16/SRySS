## Objetivo
There is a secure website running at `https://jupiter.challenges.picoctf.org/problem/29132/` ([link](https://jupiter.challenges.picoctf.org/problem/29132/)) or http://jupiter.challenges.picoctf.org:29132. Try to see if you can login as admin!
## Solución

```
En este reeto seguimos teniendo la misma pagina con la difereencia de que ahora el Admin login ya no nos pidee un usuario si no que solo una contraseña.
Al ver las pistas nos dice que al oarecer la contraseña esta encriptada.

probamos con inyeccciones basicas para ver el comportamiendo de la base de datos pero no nos muestra nada, inspeccionando el codigo encontramos un campo llamado debug,= con valor 0, lo cambiamos a valor 1 para que nos mustre los errores.


probamos contraseñas y vemos que nos lanza el mensaje:
	password: admin123
	SQL query: SELECT * FROM admin where password = 'nqzva123'
	
	Login failed.

vemos que esta encriptando lo que ponemos en contrasena, solo las letrass, viendolo parece root13, pasamoss una de las inyecciones anteriores a root13:

	nqzva' BE 1=1-- -

y de esta fomra nos da acceso a la flag
```


![Irish3PicoCTF.png](/imagenes/Irish3PicoCTF.png)

![Irish3PicoCTF(2).png](/imagenes/Irish3PicoCTF(2).png)

![Irish3PicoCTF(3).png](/imagenes/Irish3PicoCTF(3).png)
## Notas adicionales
## Referencias