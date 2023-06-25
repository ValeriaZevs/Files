Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math

a, b, c = float(input()), float(input()), float(input())
t = float(input())
print(math.degrees(math.asin(a * t / c)))
print(math.degrees(math.asin(b * t / c)))

-------------------------------------

import math

me, e, v = int(input()), int(input()), int(input())
print(v / math.log((me + e) / me))
--------------------------------------
import string
from random import randint, choice, sample


def name(n):
    surlen = randint(2, n - 2)
    namelen = n - surlen - 1
    unic = sample(string.ascii_lowercase, namelen + surlen - 1)
    sp = sample(string.ascii_lowercase[:13], 13)
    name = ''
    for i in sp:
        if i not in unic:
            name = i
            break
    sur = [unic[_] for _ in range(surlen - 1)]
    sur.insert(randint(1, surlen - 1), str(randint(0, 9)))
    sur = ''.join(sur)
    name = name + ''.join([unic[_] for _ in range(len(unic) - 1) if unic[_] not in sur])
    return sur + " " + name.capitalize()