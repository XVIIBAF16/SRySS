## Objetivo
Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_atlas/20/challenge.zip)
## Solución
```
% ssh -p 54377 ctf-player@atlas.picoctf.net
ctf-player@atlas.picoctf.net's password: 
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500
Lower! Try again.
Enter your guess: 250
Higher! Try again.
Enter your guess: 200
Higher! Try again.
Enter your guess: 300
Higher! Try again.
Enter your guess: 350
Lower! Try again.
Enter your guess: 325
Lower! Try again.
Enter your guess: 313  
Higher! Try again.
Enter your guess: 320
Lower! Try again.
Enter your guess: 319
Congratulations! You guessed the correct number: 319
Here's your flag: picoCTF{g00d_gu355_bee04a2a}
Connection to atlas.picoctf.net closed.
```
## Notas adicionales
## Referencias
