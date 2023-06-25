Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = input().split('; ')


def func(a):
    for i in a:
        return i[0] == 'V' or i[0] == 'v'


for j in a:
    d = [i for i in filter(func, a)]
    if j not in d:
        if j[0] == '*':
            print(j[1:len(j)])
        else:
            print(j)

##########################
def nearby(data, places=1):
    a = list(filter(lambda x: '0' * places in x, data))
    return a

##########################
m = int(input())
c = int(input())
h = 0
for i in range(c):
    s = list(filter(lambda x: int(x) >= m, [x for x in input().split()]))
    for a in s:
        h += int(a)
print(h)

##########################
def separator(data):
    a = list(map(lambda x: int(x), data.split(' ')))
    x = list(filter(condition, a))
    y = [i for i in a if i not in x]
    return x, y

