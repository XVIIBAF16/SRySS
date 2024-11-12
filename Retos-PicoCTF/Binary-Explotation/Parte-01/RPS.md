## Objetivo
Here's a program that plays rock, paper, scissors against you. I hear something good happens if you win 5 times in a row.The program's source code with the flag redacted can be downloaded [here](https://artifacts.picoctf.net/c/146/game-redacted.c).

Additional details will be available after launching your challenge instance.
## Solución
En este reto nos dan un comando para poder acceder al reto, asi que nos conectamos:
```
nc saturn.picoctf.net 58919
```

Vemos que nos arroja:
```
Welcome challenger to the game of Rock, Paper, Scissors
For anyone that beats me 5 times in a row, I will offer up a flag I found
Are you ready?
Type '1' to play a game
Type '2' to exit the program
```

Analizando la descripción del reto vemos que nos da el código del programa asi que lo analizamos y vemos que hay una función que compara lo que hacemos o ingresamos nosotros y lo que hace el código o la maquina, asi que guisándonos en eso ingresamos las tres palabras juntas 5 veces, es decir (rockpaperscissors):


Y a la quinta vez vemos que nos regresa la flag:
```
Please make your selection (rock/paper/scissors):
rockpaperscissors
You played: rockpaperscissors
The computer played: rock
You win! Play again?
Congrats, here's the flag!
picoCTF{50M3_3X7R3M3_1UCK_B69E01B8}
Type '1' to play a game
Type '2' to exit the program
```

Flag:
```
picoCTF{50M3_3X7R3M3_1UCK_B69E01B8}
```
## Notas adicionales
## Referencias