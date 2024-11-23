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

