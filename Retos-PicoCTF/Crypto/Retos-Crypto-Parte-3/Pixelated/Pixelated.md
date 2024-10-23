## Objetivo
I have these 2 images, can you make a flag out of them? [scrambled1.png](https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled1.png)[scrambled2.png](https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled2.png)
## Solución

En este reto nos proporcionan dos imagenes que hay que juntar para poder ver la falag:

Imagen 1
![scrambled 1](/imagenes/scrambled2.png)

Imagen 2
![scrambled 2](/imagenes/scrambled1.png)


Usando stegsolve vamos a unir las dos imagenes pero primero lo tenemos que instalar o clonar desde github:

```
wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar

chmod +x stegsolve.jar

mkdir bin

```

Ejecutamos:
```
java -jar /opt/stegsolve.jar 
```


Y en la interfaz abrimos la primera imagen y vamos a analizar y image Combiner:
![scrambled Solve](/imagenes/scrambled.png)


Y en la segunda ventana vamos avanzando con las flechas de abajo hasta encontrar la flag:
![scrambled Solve 2](/imagenes/scrambled(2).png)

y nos da la flag:
```
picoCTF{da8fcef8}
```
## Notas adicionales
## Referencias