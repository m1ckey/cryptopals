from lib.bit import *
from lib.enc import *

hx = ['1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965']

b0 = hex_to_bytes(hx[0])
b1 = hex_to_bytes(hx[1])

b = xor(b0, b1)

result = bytes_to_hex(b)
print(result)
assert result == '746865206b696420646f6e277420706c6179'
