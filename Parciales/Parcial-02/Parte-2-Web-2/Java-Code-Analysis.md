## Objetivo
BookShelf Pico, my premium online book-reading service.I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book!Here are the credentials to get you started:

- Username: "user"
- Password: "user"

Source code can be downloaded [here](https://artifacts.picoctf.net/c/479/bookshelf-pico.zip).
Website can be accessed [here!](http://saturn.picoctf.net:65446/).
## Solución
En este reto nos dan una pagina web u unas credenciales para acceder a ella, asi que accedemos y nos muestra:
![Java-Code-Analysis](/imagenes/Java-Code-Analysis.png)

Analizando la pagina vemos que hay un libro llamado flag pero no nos deja verlo ya que tenemos que ser admins.

Vemos que usa un token JWT asi que abrimos Inspeccionar y nos vamos a Application y copeamos el token:
![Java-Code-Analysis 2](/imagenes/Java-Code-Analysis(1).png)

Extraemos el token y nos vamos a la pagina jwt.io y reasignamos valores cambiando Free por Admin, email por admin, y user ID: 2:
![Java-Code-Analysis 2](/imagenes/Java-Code-Analysis(2).png)

Y lo remplazamos el token viejo por el nuevo y nos deja ver el contenido del libro y la flag:
![Java-Code-Analysis 2](/imagenes/Java-Code-Analysis(3).png)

Flag: 
```
picoCTF{w34k_jwt_n0t_g00d_d7c2e335}
```

## Notas adicionales
## Referencias