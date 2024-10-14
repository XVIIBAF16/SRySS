## Objetivo
My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/70/challenge.zip)
## Solución

```
drop-in3 % ls
flag.py
drop-in3 % cat flag.py 
print("Printing the flag...")
drop-in3 % git branch -a
  feature/part-1
  feature/part-2
  feature/part-3
* main

drop-in3 % git checkout feature/part-1
Cambiado a rama 'feature/part-1'

drop-in3 % git diff main
diff --git a/flag.py b/flag.py
index 77d6cec..6e17fb3 100644
--- a/flag.py
+++ b/flag.py
@@ -1 +1,2 @@
 print("Printing the flag...")
+print("picoCTF{t3@mw0rk_", end='')
\ No newline at end of file
drop-in3 % git checkout feature/part-2
Cambiado a rama 'feature/part-2'

drop-in3 % git diff main              
diff --git a/flag.py b/flag.py
index 77d6cec..7ab4e25 100644
--- a/flag.py
+++ b/flag.py
@@ -1 +1,3 @@
 print("Printing the flag...")
+
+print("m@k3s_th3_dr3@m_", end='')
\ No newline at end of file

drop-in3 % git checkout feature/part-3
Cambiado a rama 'feature/part-3'
fdrop-in3 % git diff main              
diff --git a/flag.py b/flag.py
index 77d6cec..456656e 100644
--- a/flag.py
+++ b/flag.py
@@ -1 +1,3 @@
 print("Printing the flag...")
+
+print("w0rk_7ffa0077}")
```
## Notas adicionales
## Referencias