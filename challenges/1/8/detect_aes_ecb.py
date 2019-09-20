from itertools import combinations

from scipy.special import comb

from lib.bit import *
from lib.enc import *

ctexts = map(lambda l: hex_to_bytes(l), open('8.txt').read().splitlines())

dikt = {}
idx = 0
for ctext in ctexts:
    slices = [ctext[i:i + 16] for i in range(0, len(ctext), 16)]
    combos = combinations(slices, 2)
    idx += 1
    hdistance = 0
    for a, b in combos:
        if len(a) != len(b):
            continue
        hdistance += hamming_distance_byte(a, b)

    dikt[ctext] = hdistance / comb(len(slices), 2)

ctexts = sorted(dikt.keys(), key=dikt.get)

print('0x' + bytes_to_hex(ctexts[0]))
assert ctexts[0].startswith(b'\xd8\x80a\x97@\xa8\xa1\x9bx@\xa8')
