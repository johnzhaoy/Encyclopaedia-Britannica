from geotext import GeoText
import pandas as pd
import os
import pycountry, pycountry_convert as pc

def read_file():
    # dirs = os.listdir(r'./edition1')
    dirs = os.listdir(r'F:\Edin\1_1\Data Science for Design\Encyclopedia Britannica\Data\Raw\nls-text-encyclopaediaBritannica\edition1')
    for file in dirs:
        fp1 = r'F:\Edin\1_1\Data Science for Design\Encyclopedia Britannica\Data\Raw\nls-text-encyclopaediaBritannica\edition1' +'\\'+ file
        f = open(fp1, encoding='utf-8')
        a = f.read()
        f.close()
        return a


def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_nam = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_nam

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
citylist = []
country_code_list = []
continent_list = []
sentence = []

def processdata(txt):
    for line in txt:
        entrylist.append(line.replace('\n', ' '))
        places = GeoText(line)
        citylist.append(", ".join(str(x) for x in places.cities))
        country_code_list.append(",".join(str(x) for x in places.country_mentions.keys()))


processdata(b)
dic = {'Entry': entrylist, 'City': citylist, 'Country code': country_code_list}
dic1 = pd.DataFrame(dic)


country_list_full = [[] for i in range(len(country_code_list))]
continent_list_full = [[] for i in range(len(country_code_list))]
print(len(country_code_list))
print(country_code_list)

for i in range(len(country_code_list)):
    country_code = country_code_list[i]
    country_code_part = country_code.split(",")
    country_list = []
    for x in country_code_part:
        try:
            country_name = pycountry.countries.get(alpha_2=x).name
            country_list.append(country_name)
        except:
            country_list.append('N/A')

    country_list_full[i] = country_list


for i in range(len(country_code_list)):
    country_code = country_code_list[i]
    country_code_part = country_code.split(",")
    continent_list = []
    for x in country_code_part:
        try:
            country_name = pycountry.countries.get(alpha_2=x).name
            continent = country_to_continent(country_name)
            continent_list.append(continent)
        except:
            continent_list.append('N/A')

    continent_list_full[i] = continent_list


dic1['Edition'] = 1
dic1['Country'] = country_list_full
dic1['Continent'] = continent_list_full
dic1.to_csv("output.csv",index=False)