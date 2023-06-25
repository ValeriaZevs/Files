Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys

data = list(map(str.strip, sys.stdin))
print(min(data, key=lambda s: (sum(map(int, s)), -len(s), int(s))))

###########################
import sys

data = list(map(str.strip, sys.stdin))
d = list(map(lambda x: x.split(';'), [i for i in data]))
c = 0
for i in d:
    if any(int(x) % 5 == 0 for x in i) is True:
        c += 1
if len(d) == c:
    print('FAIL')
else:
    print('OK')

###########################
import sys

data = list(map(str.strip, sys.stdin))
d = []
for i in data:
    j = i.split()
    s = []
    for k in j:
        if k.isdigit():
            s.append(int(k))
    d.append(s)
b = max(d, key=lambda i: len(i))
x = list(filter(lambda x: len(x) == len(b), d))
a = min(x, key=lambda i: sum(i))
if sum(a) != 0:
    print(sum(a))
else:
    print(-1)