## Objetivo
The password for the next level is stored in the file **data.txt**, which contains base64 encoded data
## Datos  acceso al nivel
```
Username: bandit10
Password: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```
## Solución
![RetoBandit10](/imagenes/Bandit10(1).png)

![RetoBandit10](/imagenes/Bandit10(2).png)
## Notas adicionales
### Forma 1
con paginas web de decode base64
- cyberchef
- base64 deode

### Forma 2
```
echo VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg== | base64 -d
	
echo: para imripmir un texto en pantalla, een este caso le pasamos la contraseña encodeada en base64.

base64 -d: decodear en base64, en este caso la contraseña encodeada.
```
## Referencias
