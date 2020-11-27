from geotext import GeoText
import pandas as pd
import os

def read_file():
    dirs = os.listdir(r'./edition1')
    for file in dirs:
        fp1 = './edition1/' + file
        f = open(fp1, encoding='utf-8')
        a = f.read()
        f.close()
        return a


'''
def read_file():
    # f = open(r"F:\Edin\1_1\Data Science for Design\Encyclopedia Britannica\Data\Raw\nls-text-encyclopaediaBritannica\193819047.txt", "r", encoding='UTF-8')
    f = open("/Users/xuang/Downloads/nls-text-encyclopaediaBritannica/194167545.txt", "r")
    a = f.read()
    f.close()
    return a
'''

a = read_file()
b = a.split(".\n")  # split the txt into entries

entrylist = []
countrylist = []


def processdata(txt):
    for line in txt:
        entrylist.append(line.replace('\n', ' '))
        places = GeoText(line)
        countrylist.append(",".join(str(x) for x in places.cities))


processdata(b)
dic = {'Entry': entrylist, 'Country': countrylist}
dic1 = pd.DataFrame(dic)
dic1['edition'] = 1
print(dic1)
