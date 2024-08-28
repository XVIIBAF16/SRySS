## Objetivo
The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions
## Datos  acceso al nivel
```
Username: bandit11
Password: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```
## Solución

![RetoBandit11](../imagenes/Bandit11(1).png)

![RetoBandit11](../imagenes/Bandit11(2).png)
## Notas adicionales
```
cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'

tr '[A-Za-z]' '[N-ZA-Mn-za-m]': Permite definir como estara compuesto el conjunto o una coleccion de caracteres y conjuntos predefinidos. 
```
## Referencias
