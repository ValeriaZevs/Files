Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json


def func(x, y):
    return x ** 2 + y ** 2


with open('input.json') as input_file:
    data = json.load(input_file)
    data.sort(key=lambda x: (-len(x['colors']),
                             -x['radius'],
                             -func(x['x'], x['y']),
                             -x['id']))
    for i in data:
        print(i['id'], end=' ')

#################################
import json

with open('in.json', 'r') as cat_file, open('out.json', 'w') as dog_file:
    data = json.load(cat_file)
    a = data['complex'][0]['Re']
    b = data['complex'][0]['Im']
    c = data['complex'][1]['Re']
    d = data['complex'][1]['Im']
    result = {'complex': [{'Re': a + c, 'Im': b + d},
                          {'Re': a - c, 'Im': b - d},
                          {'Re': a * c - b * d, 'Im': a * d + b * c}]}
    print(result)
    json.dump(result, dog_file, indent=4)

#################################
import json

rus1 = open('russian_words.txt', 'r', encoding='utf-8').readlines()
rus = [i.rstrip() for i in rus1]
with open('russian_words.json', 'w') as result:
    r = {}
    for i in rus:
        if i[0] in r:
            r[i[0]].append(i)
        else:
            r[i[0]] = []
            r[i[0]].append(i)
    json.dump(r, result, ensure_ascii=False, indent=2)

#################################
import csv
import json


with open('catalog.csv', 'r') as catalog, open('pets.json', 'w') as pets:
    data = csv.DictReader(catalog, delimiter=';')

    result = {'type': {}}

    animals = list()
    for item in data:
        type = item['type']
        result['type'][type] = {'breed': {}}
        animals.append(item)

    for animal in animals:
        type = animal['type']
        breed = animal['breed']
        if breed not in result['type'][type]['breed'].keys():
            result['type'][type]['breed'][breed] = list()
        result['type'][type]['breed'][breed].append({'name': animal['name'],
                                                     'age': animal['age'],
                                                     'gender': animal['gender'],
                                                     'owner': animal['owner'],
                                                     'phone': animal['phone']})

    json.dump(result, pets, indent=2)