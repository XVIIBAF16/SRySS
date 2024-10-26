## Objetivo
Can you get the flag?
Go to this [website](http://saturn.picoctf.net:55258/) and see what you can discover.
## Solución

En este reto nos proporcionan una pagina web que nos muestra:
![Power-Cookie](/imagenes/Power-Cookie.png)


Presionando el boton de continuar como invitado nos da el mensaje:
![Power-Cookie 1](/imagenes/Power-Cookie(1).png)


Viendo las cookies del sitio web con la extension Cookie-Editor vemos que hay una cookie llamada Admin asi que vemos su contenido y vemos que tiene un valor de 0 asi que lo cambiamos a 1:
![Power-Cookie 2](/imagenes/Power-Cookie(2).png)


Refrescando la pagina con el nuevo valor de la Cookie vemos que nos muestra la flag:
![Power-Cookie 3](/imagenes/Power-Cookie(3).png)
```
picoCTF{gr4d3_A_c00k13_65fd1e1a}
```

## Notas adicionales
## Referencias