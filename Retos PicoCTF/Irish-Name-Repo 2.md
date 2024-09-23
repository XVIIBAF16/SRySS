## Objetivo
There is a website running at `https://jupiter.challenges.picoctf.org/problem/52849/` ([link](https://jupiter.challenges.picoctf.org/problem/52849/)). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://jupiter.challenges.picoctf.org:52849
## Datos  acceso al nivel
```
Username: admin' AND 1=1-- -
Password: lo que sea
```
## Solución
```
Para este reto igual que el anterior tambien es una pagina, de hecho es la misma pagina, tambien tenemos el admin login asi que volvemos a intentar por ahi.

Probamos la inyeccion del reto anterior y vemos que no funciona asi que probamos con la segunda opcion que seria:

admin ' AND 1=1-- -

Contraseña la quee sea y vemos que si funciona y nos muestra la flag en pantalla
```


![Irish2PicoCTF.png](../../imagenes/Irish2PicoCTF.png)

![Irish2PicoCTF(2).png](../../imagenes/Irish2PicoCTF(2).png)
## Notas adicionales
## Referencias