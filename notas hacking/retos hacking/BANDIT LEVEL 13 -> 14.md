## Objetivo
The password for the next level is stored in **/etc/bandit_pass/bandit14 and can only be read by user bandit14**. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. **Note:** **localhost** is a hostname that refers to the machine you are working on

## Datos  acceso al nivel
```
Username: bandit13
Password: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```
## Solución
![RetoBandit13](../imagenes/Bandit13(1).png)
```
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
MU4VWeTyJk8R0of1qqmcBPaLh7lDCPvS
bandit14@bandit:~$
```
## Notas adicionales
```
ssh-private-key: una llave privada permite al usuario ingresar al servidor sin usar el password.

ssh -i llave: para pasarle la llave a ssh se una el parametro -i.
```
## Referencias
