## Objetivo
There is a git repository at `ssh://bandit29-git@localhost/home/bandit29-git/repo` via the port `2220`. The password for the user `bandit29-git` is the same as for the user `bandit29`.

Clone the repository and find the password for the next level.
## Datos  acceso al nivel
```
Username: bandit29
Password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7
```
## Solución
```
fabianmartinezalonso@MacBook-Pro-de-Fabian ~ % ssh bandit29@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit29@bandit.labs.overthewire.org's password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7







bandit29@bandit:~$ fma=$(mktemp -d)
bandit29@bandit:~$ cd $fma
bandit29@bandit:/tmp/tmp.JWLCnh6MBp$ git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit29/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit29/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit29-git@localhost's password: 
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 16 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (16/16), done.
Resolving deltas: 100% (2/2), done.






bandit29@bandit:/tmp/tmp.JWLCnh6MBp$ cd repo/
bandit29@bandit:/tmp/tmp.JWLCnh6MBp/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL

bandit29@bandit:/tmp/tmp.JWLCnh6MBp/repo$ git branch -a
* dev
  master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
bandit29@bandit:/tmp/tmp.JWLCnh6MBp/repo$ git checkout dev
Already on 'dev'
Your branch is up to date with 'origin/dev'.
bandit29@bandit:/tmp/tmp.JWLCnh6MBp/repo$ git branch
* dev
  master
bandit29@bandit:/tmp/tmp.JWLCnh6MBp/repo$ ls
code  README.md
bandit29@bandit:/tmp/tmp.JWLCnh6MBp/repo$ cd code/
bandit29@bandit:/tmp/tmp.JWLCnh6MBp/repo/code$ ls
gif2ascii.py
bandit29@bandit:/tmp/tmp.JWLCnh6MBp/repo/code$ cat gif2ascii.py

bandit29@bandit:/tmp/tmp.JWLCnh6MBp/repo/code$ cd ..
bandit29@bandit:/tmp/tmp.JWLCnh6MBp/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL

```
## Notas adicionales
## Referencias