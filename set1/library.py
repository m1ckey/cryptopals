import sys


def xor(byte, string):
    '''
    simple xor function
    arg0: the single byte with which arg1 should be xored
    arg1: the input string
    return: xor'ed string as bytes
    '''
    if (len(string) % 2) == 1:
        string = '0' + string

    string = bytes.fromhex(string)
    output = bytearray(len(string))
    for i, b in enumerate(string):
        output[i] = b ^ byte

    return bytes(output)


def brute(string):
    '''
    xor string with every possible extended ascii character
    arg0: string string
    return: array of all possible strings(combine with is_printable if needed)
    '''
    result = []
    for i in range(256):
        result.append(xor(i, string))
    return result


def is_printable(b):
    '''
    decide wheter a bytestring is printable or not
    arg0: bytes, unknown if they are printable
    return: true if string is printable, else false
    '''
    try:
        if r.decode().isprintable():
            return True
        else:
            return False
    except BaseException:
        return False
