import base64


def is_printable(b):
    """
    tries to decode the bytes object with UTF-8 and checks if the string is printable
    the string is printable when str.isprintable() returns True after all LF, CR, and TAB are removed

    :param b: bytes
    :return: True if bytes are printable
    """

    try:
        s = b.decode()
        s = s.translate({ord('\n'): None, ord('\r'): None, ord('\t'): None})
        return s.isprintable()
    except UnicodeError:
        return False


def is_decodable(b):
    """
    tries to decode the bytes object with UTF-8

    :param b: bytes
    :return: True if bytes are decodable
    """

    try:
        s = b.decode()
        return True
    except UnicodeError:
        return False


def hex_to_bytes(s):
    """
    tries it's best to convert a hex string to bytes
    :param s: hex string
    :return: bytes
    """

    s = s.lower().replace('0x', '')
    s = ''.join(filter(lambda c: c in '0123456789abcdef', s))

    if len(s) % 2 == 1:
        s = '0' + s

    return bytes.fromhex(s)


def bytes_to_hex(b):
    """
    converts bytes to hex string
    :param b: bytes
    :return: hex string
    """

    return b.hex()


def bytes_to_base64(b):
    """
    convert bytes to base64 string
    :param b: bytes
    :return: base64 string
    """

    return base64.b64encode(b).decode()


def base64_to_bytes(s):
    """
    convert base64 string to bytes
    :param s: base64 string
    :return: bytes
    """

    return base64.b64decode(s)
