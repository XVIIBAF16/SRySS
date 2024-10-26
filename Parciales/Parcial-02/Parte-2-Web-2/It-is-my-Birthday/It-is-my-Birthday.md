## Objetivo
I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. Anyway, see if you're invited by submitting 2 PDFs to my website. [http://mercury.picoctf.net:57247/](http://mercury.picoctf.net:57247/)
## Solución
En este reto nos proporcionan una pagina web que nos muestra:
![It-is-my-Birthday](/imagenes/It-is-my-Birthday.png)


Al parecer tenemos que subir dos archivos y guiándonos por la descripción del reto tienen que ser dos archivos md5, asi que buscamos dos archivos:
![It-is-my-Birthday 2](/imagenes/It-is-my-Birthday(1).png)


Pero al parecer la pagina solo acepta pdf asi que cambiamos la extension de los archivos a pdf y los subimos:
![It-is-my-Birthday 3](/imagenes/It-is-my-Birthday(2).png)


Y nos arroja lo que parece ser un script y en el la flag:
![It-is-my-Birthday 4](/imagenes/It-is-my-Birthday(3).png)

```
picoCTF{c0ngr4ts_u_r_1nv1t3d_40d81ca2}
```
## Notas adicionales
## Referencias
[picoCTF 2o21 — It is my birthday](https://medium.com/@pr0f_41bu5/picoctf-2021-it-is-my-birthday-writeup-85bb22864500)
[MD5 Collision Demo](https://www.mscs.dal.ca/~selinger/md5collision/)
