import sys

inputs = ['1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965']

if len(sys.argv) >= 3:
     inputs = sys.argv[1:]

longest = 0
for i, input in enumerate(inputs):
    # pad to even string
    if (len(input) % 2) == 1:
        inputs[i] = '0' + input

    # get longest
    if len(input) > longest:
        longest = len(input)

output = bytearray(int(longest / 2))
for input in inputs:
    # pad to longest
    if len(input) != longest:
        input = ('0' * (longest - len(input))) + input

    # xor
    result = output
    for i, b in enumerate(bytes.fromhex(input)):
        result[i] ^= b
    output = result

print(output.hex())
