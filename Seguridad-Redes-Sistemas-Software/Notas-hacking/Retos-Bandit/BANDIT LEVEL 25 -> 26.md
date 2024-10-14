## Objetivo
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not **/bin/bash**, but something else. Find out what it is, how it works and how to break out of it.

> NOTE: if you’re a Windows user and typically use Powershell to `ssh` into bandit: Powershell is known to cause issues with the intended solution to this level. You should use command prompt instead.
## Datos  acceso al nivel
```
Username: bandit25
Password: iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
```
## Solución
```
% ssh bandit25@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit25@bandit.labs.overthewire.org's password: 




XVIIBAF@XVIIBAF phobex % nvim llave
XVIIBAF@XVIIBAF phobex % chmod 600 llave
XVIIBAF@XVIIBAF phobex % cat llave 


- Se hace la pantalla chuca hasta ver el more...
- Se teclea v para mandarlo al editor
- esc y se teclea e /etc/bandit_pass/bandit26
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
```

```
Estando en el editor tecleamos esc y ponemos el comando:
	set shell=/bin/bash
Tecleamos esc de nuevo y ponemoss el comando:
	shell
Salida:
bandit26@bandit:~$
bandit26@bandit:~$ cat /etc/bandit_pass/bandit26
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
```
## Notas adicionales
## Referencias