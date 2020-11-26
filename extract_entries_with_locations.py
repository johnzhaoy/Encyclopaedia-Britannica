from geotext import GeoText
import pandas as pd


def read_file():
    # f = open(r"F:\Edin\1_1\Data Science for Design\Encyclopedia Britannica\Data\Raw\nls-text-encyclopaediaBritannica\193819047.txt", "r", encoding='UTF-8')
    f = open("/Users/wanfangdu/Desktop/DS4D/Project/nls-text-encyclopaediaBritannica/194167545.txt", "r")
    a = f.read()
    f.close()
    return a


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
print(pd.DataFrame(dic))
