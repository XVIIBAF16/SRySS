## Objetivo
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...
Download the image [here](https://artifacts.picoctf.net/c/302/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png)
## Solución
En este reto nos dan una imagen para analizarla, basandonos en la descripción del reto sugieren que la flag puede estar en el bit mas significativo de la imagen asi que usamos el script sigBits.py 

Lo descargamos o creamos y lo ejecutamos pasándole la imagen como parametro:
```
MSB % python3 sigBits.py -t=msb Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
Done, check the output file!
```

Hacemos un cat al archivo que nos dio:
```
MSB % cat outputSB.txt
```

Y vemos que nos regresa muchos caracteres asi que usamos el comando grep con parametros -o y -E y especificando que pude haber 50 caracteres mas después de picoCTF
```
MSB % cat outputSB.txt | grep -o -E "picoCTF.{0,50}"
picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_ea7deb4c}"Thou h
```

y nos da la flag:
```
picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_ea7deb4c}
```
## Notas adicionales
## Referencias