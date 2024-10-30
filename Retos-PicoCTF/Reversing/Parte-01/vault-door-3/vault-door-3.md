## Objetivo
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://jupiter.challenges.picoctf.org/static/a648ca6dd275b9454c5d0de6d0f6efd3/VaultDoor3.java)
## Solución
En este reto igual nos dan un script en Java que al revisar su contenido al parecer nos da la flag pero no es asi, ya que pasa por un proceso y nos da la verdadera flag, y al correr el programa nos pide una contraseña:

```
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	   System.out.println("Access granted.");
	} else {
	   System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
    }
}
```


Asi que creamos un script en python con la misma funcionalidad solo sacando la parte donde da la flag:

Script
```
flag = [None] * 32
password = 'jU5t_a_sna_3lpm18gb41_u_4_mfr340'

for i in range(0, 8):
    flag[i] = password[i]

for i in range(8, 16):
    flag[i] = password[23 - i]

for i in range(16, 32, 2):
    flag[i] = password[46 - i]

for i in range(31, 16, -2):
    flag[i] = password[i]

print("picoCTF{{{}}}".format(''.join(flag)))
```

Y al ejecutarlo nos da la flag:
```
vault-door-3 % python3 exp.py
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}
```
## Notas adicionales
## Referencias