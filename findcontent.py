import json
import requests

def read_file():
    with open("188082735.34.xml", encoding='UTF-8')as f:
        a = f.read()
    f.close()
    return a

a = read_file()
b = a.split()

output = open('content_output.csv', mode='a', encoding='utf-8')

for c in b:
    d = c.split("CONTENT=")
    if len(d) == 1:
        continue
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
    url = url+d[1][1:-1]
    response = requests.get(url)
    json_format = response.json()
    try:
        if (json_format[0]['word']):
            word = json_format[0]['word']
            if (len(word)!=1):
                print(word)
                print(word, file=output)
    except KeyError:
        print("not found!")