## Objetivo
There is a git repository at `ssh://bandit30-git@localhost/home/bandit30-git/repo` via the port `2220`. The password for the user `bandit30-git` is the same as for the user `bandit30`.

Clone the repository and find the password for the next level.
## Datos  acceso al nivel
```
Username: bandit30
Password: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL
```
## Solución
```
% ssh bandit30@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit30@bandit.labs.overthewire.org's password: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL







bandit30@bandit:~$ fmaa=$(mktemp -d)
bandit30@bandit:~$ cd $fmaa
bandit30@bandit:/tmp/tmp.2Dc2VUl85p$ git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit30/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit30/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit30-git@localhost's password: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.







bandit30@bandit:/tmp/tmp.2Dc2VUl85p$ ls
repo
bandit30@bandit:/tmp/tmp.2Dc2VUl85p$ cd repo/
bandit30@bandit:/tmp/tmp.2Dc2VUl85p/repo$ cat README.md 
just an epmty file... muahaha
bandit30@bandit:/tmp/tmp.2Dc2VUl85p/repo$ git tag
secret
bandit30@bandit:/tmp/tmp.2Dc2VUl85p/repo$ git show secret
fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy
bandit30@bandit:/tmp/tmp.2Dc2VUl85p/repo$ 
```
## Notas adicionales
## Referencias