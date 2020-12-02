from geotext import GeoText
import pandas as pd
import os
import pycountry, pycountry_convert as pc
import fnmatch


path = r'F:\Edin\1_1\Data Science for Design\Encyclopedia Britannica\Data\Raw\nls-text-encyclopaediaBritannica'
output_dir = r'F:\Edin\1_1\Data Science for Design\Encyclopedia Britannica\Coding\Encyclopaedia-Britannica\extracted'

def read_file():
    dirs = os.listdir(path)
    for file in dirs:
        fp1 = path +'\\'+ file
        f = open(fp1, encoding='utf-8')
        a = f.read()
        f.close()
    return a

def processdata(txt):
    for line in txt:
        entrylist.append(line.replace('\n', ' '))
        places = GeoText(line)
        citylist.append(", ".join(str(x) for x in places.cities))
        country_code_list.append(",".join(str(x) for x in places.country_mentions.keys()))


def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_nam = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_nam


for edition_num in range(1,9):
    files = []
    edition = "edition" + str(edition_num)
    path = path + "\\" + edition
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*.txt'):
            files.append(os.path.join(root, filename))
    print("found %d .txt files in %s" % (len(files), path))
    a = read_file()

    b = a.split(".\n")  # split the txt into entries

    entrylist = []
    citylist = []
    country_code_list = []
    continent_list = []
    sentence = []

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

    dic1['Edition'] = edition_num
    for i in range(len(country_list_full)):
        country_list_full[i] = ','.join(country_list_full[i])
        continent_list_full[i] = ','.join(continent_list_full[i])
    dic1['Country'] = country_list_full
    dic1['Continent'] = continent_list_full

    asia = pd.DataFrame(dic1[dic1['Continent'].str.contains('Asia')])

    europe = pd.DataFrame(dic1[dic1['Continent'].str.contains('Europe')])

    north_america = pd.DataFrame(dic1[dic1['Continent'].str.contains('North America')])

    south_america = pd.DataFrame(dic1[dic1['Continent'].str.contains('South America')])

    africa = pd.DataFrame(dic1[dic1['Continent'].str.contains('Africa')])

    antarctica = pd.DataFrame(dic1[dic1['Continent'].str.contains('Antarctica')])

    oceania = pd.DataFrame(dic1[dic1['Continent'].str.contains('Oceania')])

    dirName = output_dir + "\\" + edition
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    dirName = dirName + "\\"
    dic1.to_csv(dirName + "output.csv",index=False)
    asia.to_csv(dirName + "asia.csv",index=False)
    europe.to_csv(dirName + "europe.csv",index=False)
    north_america.to_csv(dirName + "north_america.csv",index=False)
    south_america.to_csv(dirName + "south_america.csv",index=False)
    africa.to_csv(dirName + "africa.csv",index=False)
    oceania.to_csv(dirName + "oceania.csv",index=False)
    antarctica.to_csv(dirName + "antarctica.csv",index=False)

    path = path.split(edition, 1)[0]

