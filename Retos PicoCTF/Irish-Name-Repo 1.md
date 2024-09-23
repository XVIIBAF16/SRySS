## Objetivo

There is a website running at `https://jupiter.challenges.picoctf.org/problem/39720/` ([link](https://jupiter.challenges.picoctf.org/problem/39720/)) or http://jupiter.challenges.picoctf.org:39720. Do you think you can log us in? Try to see if you can login!
## Datos  acceso al nivel
```
Username: admin' OR 1=1-- -
Password: lo que sea
```
## Solución

```
Para este reto no encontramos con una oagina web la cual inspeccionandola enconramos un login de admin ene ella.
Leyendo las pistas del reto nos damos cuenta que esta tiene inyeccioness sql o vulnerabilidades sql las cuales podemos aprovechar para logearse facilemnte


probamos la inyeccion basica en un login que es

USERNAME:
admin ' OR 1=1-- -

PASSWORD:
lo que sea

y asi es como se gana acceso a la bandera en este reto
```



![Irish1PicoCTF(1).png](/imagenes/Irish1PicoCTF(1).png)

![Irish1PicoCTF.png](/imagenes/Irish1PicoCTF.png)
## Notas adicionales
## Referencias