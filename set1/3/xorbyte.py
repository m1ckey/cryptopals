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
    strings=open('set.txt', 'r').read()
    strings=filter(None, strings.split('\n')) # delete empty strings
    for string in strings: 
        result = brute(string)
        #for i, r in enumerate(result):
            #print('%02x : %s' % (i, str(r)[2:-1]))

        print()
        print('printable:')
        for i, r in enumerate(result):
            if is_printable(r):
                print('%02x : %s' % (i, r.decode()))
