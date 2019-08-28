from lib.bit import *
from lib.enc import *

key = 'ICE'
key = key.encode()

text = 'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
text = text.encode()

cipher_text = xor(key, text)

result = bytes2hex(cipher_text)

print(bytes2hex(cipher_text))

assert result == '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
