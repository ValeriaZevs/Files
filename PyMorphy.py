Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pymorphy2
import sys

data = list(map(str.strip, sys.stdin))
morph = pymorphy2.MorphAnalyzer()

for phrase in data:
    phrase = phrase.split()
    noun = phrase[0]
    adjective = phrase[1]
    if morph.parse(phrase[0])[0].tag.POS != 'NOUN':
        noun = phrase[1]
        adjective = phrase[0]
    n = morph.parse(noun)[0]
    a = morph.parse(adjective)[0]
    tags = {n.tag.number, n.tag.case}
    if n.tag.number == 'sing':
        tags = tags.union({n.tag.gender})
    print(a.inflect(tags).word, noun)
-------------------------------------
import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def participle(w, **args):
    args = dict(args)
    word = morph.parse(w)[0]
    a = ['PRTF']
    for i in list(args.values()):
        a.append(i)
    return word.inflect(set(a)).word
--------------------------------------
import pymorphy2
import sys

data = list(map(str.strip, sys.stdin))
morph = pymorphy2.MorphAnalyzer()

data2 = []
for i in data:
    s = ''
    m = '!.?,—:"'
    for j in i:
        if j in m:
            continue
        else:
            s += j
    data2.append(s)


def verb(word):
    return word.tag.POS == 'VERB' or word.tag.POS == 'INFN'


perf, imperf = set(), set()
for i in data2:
    str = i.split()
    if len(str) == 0:
        continue
    else:
        for elem in str:
            word1 = morph.parse(elem)
            word1 = list(filter(verb, word1))
            if len(word1) == 0:
                continue
            word = word1[0]
            if (word.tag.POS == 'VERB' or word.tag.POS == 'INFN') and word.tag.aspect == 'perf':
                perf.add(word.normal_form)
            if (word.tag.POS == 'VERB' or word.tag.POS == 'INFN') and word.tag.aspect == 'impf':
                imperf.add(word.normal_form)

perf, imperf = sorted(list(perf)), sorted(list(imperf))
imperf.extend(perf)
for i in imperf:
    print(i)