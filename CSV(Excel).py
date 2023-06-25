Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys

with open('plantis.csv', 'w', encoding='utf-8') as file:
    data = [line.strip().split('\t') for line in sys.stdin]
    print(*data, sep='\n')

    print('nomen;definitio;pluma;Russian nomen;familia;Russian nomen familia', file=file)
    for line in data:
        print(';'.join(line), file=file)

#################################
import csv

name = input()
years = input().split()

with open('salary.csv', 'r', encoding='utf-8') as catalog, open('out_file.csv', 'w') as result:
    reader = csv.DictReader(catalog, delimiter=';')
    writer = csv.writer(result, delimiter=";")
    t = 0
    for key in reader:
        for keys in key:
            if key.get(keys) == name:
                if (int(key.get(years[1])) - int(key.get(years[0]))) / int(key.get(years[0])) < 0.04 and t == 0:
                    t += 1
                    fieldnames = ['Субъект', years[0], years[1]]
                    print(';'.join(fieldnames), file=result)
                    writer.writerow([key.get('Субъект'), key.get(years[0]), key.get(years[1])])
                elif (int(key.get(years[1])) - int(key.get(years[0]))) / int(key.get(years[0])) < 0.04 and t != 0:
                    writer.writerow([key.get('Субъект'), key.get(years[0]), key.get(years[1])])
    if t == 0:
        writer.writerow('')

##################################
import csv


def messier_search(param):
    spisok = {i[param] for i in csv.DictReader(open('messier.csv'), delimiter=';') if i[param]}
    return sorted(spisok)