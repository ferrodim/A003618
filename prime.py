from bitarray import bitarray
import sys
import math

mul = int(sys.argv[1])

limit = math.ceil(10 ** mul)
datFile = open('eratosthenes.' + str(mul) + '.bin', 'rb')
p = bitarray()
p.fromfile(datFile)
# limit = p.size
print('p.size', len(p))

m = math.floor(mul * 2)
while m > 1:
    t = 10 ** m - 1
    limit = math.ceil(10 ** (m / 2))
    i = 3
    while i < limit:
        if (p[i] and t % i == 0):
            print(t, 'can be divided by', i)
            i = 3
            t -= 2
            continue
        i += 2
    print(t, 'is a biggest', m, 'digit prime')
    m -= 1
