from lib.cipher import *

ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
ciphertext = hex_to_bytes(ciphertext)

result = solve_single_byte_xor_cipher(ciphertext)

print(result)
assert result == "Cooking MC's like a pound of bacon"
