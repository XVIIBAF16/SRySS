## Objetivo
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn 
[http://mercury.picoctf.net:34588/](http://mercury.picoctf.net:34588/)
## Solución
En este reto nos dan una pagina web que nos muestra:
![Who-are-you](/imagenes/Who-are-you.png)

Interceptamos con BurpSuite la pagina
![Who-are-you 2](/imagenes/Who-are-you(1).png)

Y una vez en Burp cambiamos los valores de User-Agent a picobrowser:
![Who-are-you 2](/imagenes/Who-are-you(1).png)

Y nos da:
![Who-are-you 2](/imagenes/Who-are-you(1)2.png)






Y seguimos, ahora agregamos Referer y link de la pagina:
![Who-are-you 2](/imagenes/Who-are-you(2).png)

y nos da:
![Who-are-you 2](/imagenes/Who-are-you(2)2.png)




En base a esa info agregamos Date y la fecha que nos da:
![Who-are-you 2](/imagenes/Who-are-you(3).png)

y nos da:
![Who-are-you 2](/imagenes/Who-are-you(3)2.png)




y ahora agregamos DNT: true:
![Who-are-you 2](/imagenes/Who-are-you(4).png)

y nos da:
![Who-are-you 2](/imagenes/Who-are-you(4)2.png)




Ahora agregamos X-Forwarded-For: 31.3.152.55:
![Who-are-you 2](/imagenes/Who-are-you(5).png)

y nos da:
![Who-are-you 2](/imagenes/Who-are-you(5)2.png)




Ahora agregamos Accept-Language: sv,en;q=0.9nnection: keep-alive:
![Who-are-you 2](/imagenes/Who-are-you(6).png)

y nos da la flag:
![Who-are-you 2](/imagenes/Who-are-you(6)2.png)

Flag:
```
picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_79e451a7}
```
## Notas adicionales
## Referencias
[Who are you?](https://ctftime.org/writeup/26905)