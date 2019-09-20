from lib.cipher import *
from lib.txt import *

lines = open('set.txt').readlines()

candidates = []
for l in lines:
    b = hex_to_bytes(l)
    candidates += brute_single_byte_xor_chiper(b)

results = order_by_test_score(candidates, simple_char_score_test)

print(results[0])
assert results[0] == 'Now that the party is jumping\n'
