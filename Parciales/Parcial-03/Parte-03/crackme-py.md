## Objetivo
[crackme.py](https://mercury.picoctf.net/static/b7cabaae6561256c50728d3515db3058/crackme.py)
## Solución
En este reto nos dan un archivo python, lo analizamos con cat para ver su contenido:
```
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE07b34c`_6N"
# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
def decode_secret(secret):
    """ROT47 decode
    NOTE: encode and decode are the same operation in the ROT cipher family.
    """
    # Encryption key
    rotate_const = 47
    # Storage for decoded secret
    decoded = ""
    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]
    print(decoded)
def choose_greatest():
    """Echo the largest of the two numbers given by the user to the program
    Warning: this function was written quickly and needs proper error handling
    """
    user_value_1 = input("What's your first number? ")
    user_value_2 = input("What's your second number? ")
    greatest_value = user_value_1 # need a value to return if 1 & 2 are equal
    if user_value_1 > user_value_2:
        greatest_value = user_value_1
    elif user_value_1 < user_value_2:
        greatest_value = user_value_2
    print( "The number with largest positive magnitude is "
        + str(greatest_value) )
choose_greatest()
```

Asi que como dice eel nombre del reto lo intentamos crackear creando un script modificado decodificación ROT47, `bezos_cc_secret` es decodificada utilizando el cifrado ROT47 y se imprime el valor original, La función `choose_greatest` solicita al usuario dos números, los compara correctamente (como enteros) y muestra cuál es el mayor.

Nuevo script:
```
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE07b34c`_6N"
# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def decode_secret(secret):
    """ROT47 decode"""
    # Encryption key
    rotate_const = 47
    decoded = ""
    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]
    print("Decoded secret:", decoded)
def choose_greatest():
    """Echo the largest of the two numbers given by the user to the program"""
    try:
        user_value_1 = int(input("What's your first number? "))  # Convert to int
        user_value_2 = int(input("What's your second number? "))  # Convert to int
        greatest_value = user_value_1  # Set the first number as default

        if user_value_1 > user_value_2:
            greatest_value = user_value_1
        elif user_value_1 < user_value_2:
            greatest_value = user_value_2
        print("The number with the largest positive magnitude is " + str(greatest_value))
    except ValueError:
        print("Please enter valid integers.")
# Decode the secret
decode_secret(bezos_cc_secret)
# Call the choose_greatest function
choose_greatest()
```

Lo ejecutamos:
```
python3 script.py 
Decoded secret: picoCTF{1|\/|_4_p34|\|ut_f3bc410e}
What's your first number? 
```

Flag:
```
picoCTF{1|\/|_4_p34|\|ut_f3bc410e}
```
## Notas adicionales
## Referencias