## Objetivo
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

**NOTE:** Try connecting to your own network daemon to see if it works as you think
## Datos  acceso al nivel
```
Username: bandit20
Password: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```
## Solución
```
% ssh bandit20@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit20@bandit.labs.overthewire.org's password:
```

```
bandit20@bandit:~$ ./suconnect 4444
```

```
ls
suconnect
bandit20@bandit:~$ nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on 127.0.0.1 48686
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
EeoULMCra2q0dSkYj561DX7s1CpBuOBt
```
## Notas adicionales
## Referencias