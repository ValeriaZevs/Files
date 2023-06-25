Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys

data = list(map(str.strip, sys.stdin))
a = []
for i in data:
    for j in i.split():
        if j[-1] in '.,:;':
            a.append(j[:-1])
        else:
            a.append(j)
n = []
f = []
for i, val in enumerate(a, start=0):
    if val[0].isupper() and val not in n:
        n.append(val)
        f.append(f'{i} - {val}')
print(*sorted(f, key=lambda s: s.split()[-1]), sep='\n')

####################################
import sys

data = []

for i in sys.stdin:
    a = []
    for j in i.split():
        a.append(int(j))
    data.append(a)

a = all([sum(x) == sum(data[0]) for x in data])
b = all([sum(x) == sum(data[0]) for x in list(zip(*data))])
if a and b:
    print('YES')
else:
    print('NO')

####################################
from functools import reduce
import math
import sys

data = list(map(str.strip, sys.stdin))
data2 = [int(i) for i in data]
k = reduce(lambda a, b: math.gcd(a, b), data2)
print(k)