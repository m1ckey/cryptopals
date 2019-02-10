import sys


def xor(byte, string):
    if (len(string)) % 2 == 1:
        string = '0' + string

    string = bytes.fromhex(string)
    output = bytearray(len(string))
    for i, b in enumerate(string):
        output[i] = b ^ byte

    return bytes(output)


def brute(string):
    result = []

    for i in range(256):
        result.append(xor(i, string))

    return result


def is_printable(r):
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
                print('%02x : %s' % (i, r.decode()))

    elif len(sys.argv) == 2:
        input = bytes.fromhex((sys.argv[1]))
        result = brute(input)

        for i, r in enumerate(result):
            print('%02x : %s' % (i, str(r)[2:-1]))

        print()
        print('printable:')
        for i, r in enumerate(result):
            if is_printable(r):
                print('%02x : %s' % (i, r.decode()))

    elif len(sys.argv) == 3:
        byte = int(sys.argv[1], 16) & 0xff
        input = sys.argv[2]
        print(xor(byte, input))
