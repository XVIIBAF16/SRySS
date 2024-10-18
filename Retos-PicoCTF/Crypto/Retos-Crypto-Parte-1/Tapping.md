## Objetivo
Theres tapping coming in from the wires. What's it saying `nc jupiter.challenges.picoctf.org 48247`.
## Solución

```
En este reto de nuevo nos proporcionan un comando para conectarnos por nc asi que nos conectamos para ver que nos arroja:
```

```
Tapping % nc jupiter.challenges.picoctf.org 48247
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .---- ..--- -.... .---- ....- ...-- ---.. .---- ---.. .---- }
```

```
Al parecer nos da la flag eencriptada en codigo morse asi que vamos a la pagina de cyberchef y la desencriptamos:
```

![Tapping](/imagenes/Tapping.png)

```
Y nos da la flag desencriptada, le damos formato y la metemos a la pagina:
picoCTf{M0RS3C0D31SFUN1261438181}
```
## Notas adicionales
## Referencias