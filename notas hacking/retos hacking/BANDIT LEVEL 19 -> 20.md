## Objetivo
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.
## Datos  acceso al nivel
```
Username: bandit19
Password: cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
```
## Solución
```
ssh bandit19@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit19@bandit.labs.overthewire.org's password:
```

```
bandit19@bandit:~$ ls -l
total 16
-rwsr-x--- 1 bandit20 bandit19 14880 Jul 17 15:57 bandit20-do
bandit19@bandit:~$ ./bandit20-do whoami
bandit20
bandit19@bandit:~$ ./bandit20-do sh -p
$ cd /etc/bandit_pass
$ cat bandit20
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
$ 
```
## Notas adicionales
## Referencias