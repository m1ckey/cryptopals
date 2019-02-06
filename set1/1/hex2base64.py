import base64
import sys


hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

if len(sys.argv) == 2:
    hex = sys.argv[1]

bytes = bytearray.fromhex(hex)
b64 = base64.b64encode(bytes).decode()

print(b64)
