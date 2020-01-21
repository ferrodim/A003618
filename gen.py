from bitarray import bitarray
import sys
import math

mul = int(sys.argv[1])
limit = math.ceil(10 ** mul)
p = bitarray(limit)
p.setall(True)

maxDivider = math.ceil(math.sqrt(limit))
i = 3
lastKnownPrime = 3
while i < maxDivider:
    if p[i]:
        j = i * lastKnownPrime
        while j < limit:
            p[j] = False
            j += i * 2
        lastKnownPrime = i
    i += 2
print('... Eratosthenes sieve done')

saveFile = open('eratosthenes.' + str(mul) + '.bin', 'wb')
p.tofile(saveFile)
