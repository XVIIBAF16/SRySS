## Objetivo
In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/b9ddda080c56fb421bf30409bec3460d/values)
## Solución

En este reto nos dan un archivo con valores rsa dentro y nos piden des encriptarlo, vemos lo que hay que hacer y empezamos factorizando n para sacar p y q con la pagina: factorDB:

![Mind-your-Ps-and-Qs](/imagenes/Mind-your-Ps-and-Qs.png)


y en python hacemos las operaciones para sacar n:
![Mind-your-Ps-and-Qs 2](/imagenes/Mind-your-Ps-and-Qs(1).png)


Ahora sacamos tn:
![Mind-your-Ps-and-Qs 2](/imagenes/Mind-your-Ps-and-Qs(2).png)


Ahora sacamos d y m:
![Mind-your-Ps-and-Qs 2](/imagenes/Mind-your-Ps-and-Qs(3).png)

Y terminamos pero no muestra la bandera como tal asi que aplicamos el comando para transformarla a hexadecimal:
```
bytes.fromhex( hex(m)[2:]).decode()
```
![Mind-your-Ps-and-Qs 2](/imagenes/Mind-your-Ps-and-Qs(4).png)

Y nos regresa la flag:
```
picoCTF{sma11_N_n0_g0od_73918962}
```
## Notas adicionales
## Referencias
[FactorDB](https://factordb.com/index.php?query=1584586296183412107468474423529992275940096154074798537916936609523894209759157543)