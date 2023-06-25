Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> out_file = open("out_file.txt", 'w')
with open("in_file.txt") as file:
    in_file = open("in_file.txt")
    s = list(map(str.rstrip, in_file.readlines()))
    for i in s:
        out_file.write(i + ' = ' + str(eval(i)) + '\n')
    out_file.close()

#################################
import sys

a = input()
data = list(map(str.strip, sys.stdin))
data2 = []
for i in data:
    j = i.split(' ')
    data2.append(j)
with open(a, 'r') as file:
    result = open('result.txt', 'w')
    letters = file.readlines()
    print(file.read())
    for i in data2:
        s = ''
        for each in i:
            for j in letters:
                t = j.split()
                if t[1] == each:
                    s += t[0]
        result.write(s + '\n')
    result.close()

##################################
with open('pipes.txt', 'r') as f:
    f = f.readlines()
    f = [i.rstrip() for i in f if i.rstrip() != '']
    v = 0
    for i in f[-1].split(' '):
        v += 1 / float(f[int(i) - 1])
    f2 = open('time.txt', 'w')
    print(60 / v, file=f2)