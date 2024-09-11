## Objetivo
The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:

- human-readable
- 1033 bytes in size
- not executable
## Datos  acceso al nivel
```
Username: bandit6
Password: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```
## Solución
![RetoBandit6](Bandit6(1).png)

![RetoBandit6](Bandit6(2).png)
## Notas adicionales
```
find / -user bandit7 -group bandit6 -size 33c 2> /dev/null
	/: para buscar archivos en la raiz.
	-user bandit7: para buscar a que usuaerio pertenece el archivo.
	-group bandit6: para buscar a que grupo pertenece el archivo.
	-size 33c: tamaño del archivo, een este caso de 33 bytes.
	- 2> /dev/null: manda los errores al null para no mostrarlos.
```
## Referencias
