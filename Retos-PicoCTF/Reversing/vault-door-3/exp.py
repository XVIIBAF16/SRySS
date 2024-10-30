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

