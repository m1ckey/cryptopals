import sys


def xor(byte, input):
    if (len(input) % 2) == 1:
        input = '0' + input

    input = bytes.fromhex(input)
    output = bytearray(len(input))
    for i, b in enumerate(input):
        output[i] = b ^ byte

    return bytes(output)


def brute(input):
    result = []

    for i in range(256):
        result.append(xor(i, input))

    return result


def is_printable(b):
    try:
        if r.decode().isprintable():
            return True
        else:
            return False
    except Exception as e:
        return False


if __name__ == '__main__':

    if len(sys.argv) == 1:
        input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        result = brute(input)

        for i, r in enumerate(result):
            print('%02x : %s' % (i, str(r)[2:-1]))

        print()
        print('printable:')
        for i, r in enumerate(result):
            if is_printable(r):
                print('%02x : %s' % (i, str(r)[2:-1]))

    elif len(sys.argv) == 2:
        input = bytes.fromhex((sys.argv[1]))
        result = brute(input)

        for i, r in enumerate(result):
            print('%02x : %s' % (i, str(r)[2:-1]))

    elif len(sys.argv) == 3:
        byte = int(sys.argv[1], 16) & 0xff
        input = sys.argv[2]
        print(xor(byte, input))
