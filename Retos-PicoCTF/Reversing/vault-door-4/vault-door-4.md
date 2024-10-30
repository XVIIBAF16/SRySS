## Objetivo
This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://jupiter.challenges.picoctf.org/static/09d3002ae349631324a17e2255ae8df2/VaultDoor4.java)
## Solución
En este reto nos proporcionan un script en Java que al ver su contenido nos damos cuenta que la flag esta encriptada y al correr el programa nos pide una contraseña:

```
import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
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

    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
    //
    //  .:::.   .:::.
    // :::::::.:::::::
    // :::::::::::::::
    // ':::::::::::::'
    //   ':::::::::'
    //     ':::::'
    //       ':'
    // -Minion #7781
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0143, 061 ,
            '9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
}
```

Asi que creamos un script en Python con la misma funcionalidad solo sacando la parte donde da la flag:

Script:
```
passBytes = [None] * 32
myBytes = [
    106, 85, 53, 116, 95, 52, 95, 98,
    '0x55', '0x6e', '0x43', '0x68', '0x5f', '0x30', '0x66', '0x5f',
    '0o142', '0o131', '0o164', '0o63', '0o163', '0o137', '0o143', '0o61',
    '9', '4', 'f', '7', '4', '5', '8', 'e',
]

for i in range(0, 8):
    passBytes[i] = chr(myBytes[i])

for i in range(8, 16):
    passBytes[i] = chr(int(myBytes[i], 16))

for i in range(16, 24):
    passBytes[i] = chr(int(myBytes[i], 8))

for i in range(24, 32):
    passBytes[i] = myBytes[i]

print("picoCTF{{{}}}".format(''.join(passBytes)))
```

Y nos regresa la flag:
```
vault-door-4 % python3 exp.py 
picoCTF{jU5t_4_bUnCh_0f_bYt3s_c194f7458e}
```
## Notas adicionales
## Referencias