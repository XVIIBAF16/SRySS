## Objetivo
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://jupiter.challenges.picoctf.org/static/ff2585f7afd21b81f69d2fbe37c081ae/VaultDoor1.java)
## Solución
Este reto nos proporciona un script en Java que al parecer imprime la flag pero al tratar de ejecutarlo pide contraseña, haciendo un cat el archivo vemos el código:

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

Asi que hacemos un script en python con la misma funcionalidad solo sacando la parte donde da la flag:

Script:
```
flag = [None] * 32

flag[0]  = 'd'
flag[29] = '9'
flag[4]  = 'r'
flag[2]  = '5'
flag[23] = 'r'
flag[3]  = 'c'
flag[17] = '4'
flag[1]  = '3'
flag[7]  = 'b'
flag[10] = '_'
flag[5]  = '4'
flag[9]  = '3'
flag[11] = 't'
flag[15] = 'c'
flag[8]  = 'l'
flag[12] = 'H'
flag[20] = 'c'
flag[14] = '_'
flag[6]  = 'm'
flag[24] = '5'
flag[18] = 'r'
flag[13] = '3'
flag[19] = '4'
flag[21] = 'T'
flag[16] = 'H'
flag[27] = '5'
flag[30] = '2'
flag[25] = '_'
flag[22] = '3'
flag[28] = '0'
flag[26] = '7'
flag[31] = 'e'

print("picoCTF{{{}}}".format(''.join(flag)))
```

Y al ejecutarlo nos da la flag:
```
vault-door-1 % python3 exp.py 
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}
```
## Notas adicionales
## Referencias