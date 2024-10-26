## Objetivo
We have several pages hidden. Can you find the one with the flag?

The website is running [here](http://saturn.picoctf.net:59553/).
## Solución
En este reto nos proporcionan una pagina web la cual al ingresar nos muestra:
![Secrets](/imagenes/Secrets.png)



Indagando un poco por la pagina web encontramos que hay una carpeeta llamada secrets:
![Secrets 1](/imagenes/Secrets(1).png)


Asi que desde el link accedemos a ella usando ../../secret/ y nos muestra:
![Secrets 2](/imagenes/Secrets(2).png)


Volvemos a revisar las carpetas desde inspeccionar y encontramos una carpeta llamada hidden, asi que entramos agregando al link /hidden/ y nos muestra un login:
![Secrets 3](/imagenes/Secrets(3).png)



Volvemos a revisar las carpetas de la pagina desde inspeccionar y encontramos una carpeta llamada superhidden asi que entramos en ella agregando al link /superhidden/ y nos muestra:
![Secrets 4](/imagenes/Secrets(4).png)


Vemos los archivos de la pagina y buscando por el archivo superhidden/ encontramos la flag:
![Secrets 5](/imagenes/Secrets(5).png)
```
picoCTF{succ3ss_@h3n1c@10n_39849bcf}
```
## Notas adicionales
## Referencias