from itertools import *

from lib.bit import *
from lib.enc import *
from lib.txt import *


def brute_single_byte_xor_chiper(b):
    """
    brute single byte xor cipher and expect utf-8 text
    :param b: bytes
    :return: list of possible results
    """

    candidates = []
    for candidate in brute_byte_xor(b):
        if is_decodable(candidate):
            candidates.append(candidate.decode())

    return candidates


def solve_single_byte_xor_cipher(ciphertext):
    """
    solve single byte xor cipher opinionated and return the best solution
    :param ciphertext: bytes
    :return: best solution, or None
    """

    candidates = brute_single_byte_xor_chiper(ciphertext)
    results = order_by_test_score(candidates, chi_squared_test, ascending=True)
    return results[0] if len(results) > 0 else None


def solve_repeating_xor_cipher(ciphertext, keysize_min=1, keysize_max=64, limit=1):
    """
    solve repeating byte xor cipher opinionated and return the best solutions
    :param ciphertext: bytes
    :param keysize_min: min keysize (inclusive)
    :param keysize_max: max keysize (inclusive)
    :param limit: max solutions (completeness-time trade-off)
    if 0 return all
    :return: string-bytes tuple list, resulting text and the key (best solution first)
    :rtype: list[(str, bytes)]
    """

    def get_block(index, length):
        if index * length >= len(ciphertext):
            raise Exception('index out of bounds')
        return ciphertext[index * length:(index + 1) * length]

    def get_blocks(length):
        rows = []
        for i in range(0, len(ciphertext), length):
            rows.append(ciphertext[i:i + length])
        return rows

    def get_slice(index, length):
        if index >= length or length >= len(ciphertext):
            raise Exception('index out of bounds')
        return ciphertext[index::length]

    def get_slices(length):
        cols = []
        for i in range(length):
            cols.append(get_slice(i, length))
        return cols

    keysize_probability = {}
    for keysize in range(keysize_min, keysize_max + 1):
        distance = 0

        blocks = get_blocks(keysize)[:4]
        combos = combinations(blocks, 2)
        for (a, b) in combos:
            distance += hamming_distance_byte(a, b)

        keysize_probability[keysize] = distance / keysize

    keysize_probability = sorted(keysize_probability, key=keysize_probability.get)

    results = []
    for keysize in keysize_probability:
        slices = get_slices(keysize)

        slice_results = []
        for slice_ in slices:
            slice_results.append(solve_single_byte_xor_cipher(slice_))

        result = []
        for i in range(len(slice_results[0])):
            for slice_result in slice_results:
                result.append(slice_result[i] if i < len(slice_result) else '')

        result = ''.join(result)
        results.append((result, xor(get_block(0, keysize), result[:keysize].encode())))
        if limit != 0 and len(results) >= limit:
            break

    return results
