import base64

encoded = (
    'JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm'
    'JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2'
    'JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1'
)
data = base64.b64decode(encoded).decode('utf-8')
data = data.replace('%', ' 0x')
ch = data.split(" ")

print('picoCTF{', end='')
for c in ch:
    if c != '':
        print(chr(int(c, 16)), end='')
print('}')

