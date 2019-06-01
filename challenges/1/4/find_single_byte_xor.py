from lib.bit import *
from lib.enc import *
from lib.txt import *

lines = open('set.txt').readlines()

candidates = []
for l in lines:
    b = hex2bytes(l)
    for candidate in xor_brute_byte(b):
        if is_printable(candidate):
            candidates.append(candidate.decode())

chi_score = {}
for c in candidates:
    chi_score[c] = chi_squared_test(c.lower())

results = sorted(chi_score.keys(), key=chi_score.get)

print(results[1])

assert results[1] == 'Now that the party is jumping\n'
