from lib.bit import *
from lib.enc import *
from lib.txt import *

inpt = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
inpt = hex2bytes(inpt)

candidates = []
for candidate in xor_brute_byte(inpt):
    if is_decodable(candidate):
        candidates.append(candidate.decode())

chi_score = {}
for c in candidates:
    chi_score[c] = chi_squared_test(c.lower())

results = sorted(chi_score.keys(), key=chi_score.get)

print(results[0])

assert results[0] == "Cooking MC's like a pound of bacon"
