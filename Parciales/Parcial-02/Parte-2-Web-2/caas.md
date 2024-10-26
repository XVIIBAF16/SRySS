## Objetivo
Now presenting 
[cowsay as a service](https://caas.mars.picoctf.net/)
## Solución
En este reto nos dan lo que parece ser una pagina web que nos muestra el mensaje:
![caas](/imagenes/caas.png)

Al parecer lo que pongamos al final de la url lo mostrara junto con un dibujo de una vaca:
![caas 2](/imagenes/caas(1).png)

Asi que intentamos una inyeccion de comandos usando ;ls despues del mensaje para ver si lo interpreta y vemos que si, nos muestra:
![caas 3](/imagenes/caas(2).png)

Vemos que hay un archivo llamado falg.txt asi que le hacemos un cat para ver su contenido:
![caas 4](/imagenes/caas(3).png)

Y encontramos la flag:
```
picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}
```
## Notas adicionales
## Referencias