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
for i in range(len(country_list_full)):
    country_list_full[i] = ','.join(country_list_full[i])
    continent_list_full[i] = ','.join(continent_list_full[i])
dic1['Country'] = country_list_full
dic1['Continent'] = continent_list_full

asia = pd.DataFrame(dic1[dic1['Continent'].str.contains('Asia')])
print(asia.head())

europe = pd.DataFrame(dic1[dic1['Continent'].str.contains('Europe')])
print(asia.head())

north_america = pd.DataFrame(dic1[dic1['Continent'].str.contains('North America')])
print(asia.head())

south_america = pd.DataFrame(dic1[dic1['Continent'].str.contains('South America')])
print(asia.head())

africa = pd.DataFrame(dic1[dic1['Continent'].str.contains('Africa')])
print(asia.head())

antarctica = pd.DataFrame(dic1[dic1['Continent'].str.contains('Antarctica')])
print(asia.head())

oceania = pd.DataFrame(dic1[dic1['Continent'].str.contains('Oceania')])
print(asia.head())
#
dic1.to_csv("output.csv",index=False)
asia.to_csv("asia.csv",index=False)
europe.to_csv("europe.csv",index=False)
north_america.to_csv("north_america.csv",index=False)
south_america.to_csv("south_america.csv",index=False)
africa.to_csv("africa.csv",index=False)
oceania.to_csv("oceania.csv",index=False)
antarctica.to_csv("antarctica.csv",index=False)