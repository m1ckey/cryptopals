def xor(b0, b1):
    """
    xor, if one is shorter it is repeated
    :param b0: bytes
    :param b1: bytes
    :return: xor'ed bytes
    """

    length = len(b0) if len(b0) >= len(b1) else len(b1)
    output = bytearray(length)

    for i in range(length):
        output[i] = b0[i % len(b0)] ^ b1[i % len(b1)]

    return output


def xor_ljust(b0, b1):
    """
    xor, if one is shorter it is adjusted to the left and filled with null bytes
    :param b0:
    :param b1:
    :return: xor'ed bytes
    """

    # dont simply adjust it because python is stupid and would create a copy
    length = len(b0) if len(b0) >= len(b1) else len(b1)
    if len(b0) < length:
        b0 = b0.ljust(length, b'\0')
    if len(b1) < length:
        b1 = b1.ljust(length, b'\0')

    return xor(b0, b1)


def xor_rjust(b0, b1):
    """
    xor, if one is shorter it is adjusted to the right and filled with null bytes
    :param b0:
    :param b1:
    :return: xor'ed bytes
    """

    # dont simply adjust it because python is stupid and would create a copy
    length = len(b0) if len(b0) >= len(b1) else len(b1)
    if len(b0) < length:
        b0 = b0.rjust(length, b'\0')
    if len(b1) < length:
        b1 = b1.rjust(length, b'\0')

    return xor(b0, b1)


def xor_brute_byte(b):
    """
    xor bytes with every byte (0x00 - 0xff)
    :param b: bytes
    :return: list of every possibility
    """

    result = []
    for i in range(256):
        result.append(xor(b, bytes([i])))
    return result
