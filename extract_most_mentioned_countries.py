import heapq
import os
import pandas as pd
import pycountry, pycountry_convert as pc

# path = r'/Users/wanfangdu/Desktop/DS4D/projectgit/extracted/edition'
path = r'F:\Edin\1_1\Data Science for Design\Encyclopedia Britannica\Coding\Encyclopaedia-Britannica\extracted\edition'
output_dir = r'F:\Edin\1_1\Data Science for Design\Encyclopedia Britannica\Coding\Encyclopaedia-Britannica\continent-related content\most_mentioned_countries'



def country_to_continent(country_alpha2):
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_nam = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_nam


def find_most_mentioned_countries(file, edition_num, continent):
    continent = os.path.splitext(continent)[0]

    if continent == "asia":
        continent = "Asia"
    if continent == "north_america":
        continent = "North America"
    if continent == "south_america":
        continent = "South America"
    if continent == "africa":
        continent = "Africa"
    if continent == "europe":
        continent = "Europe"
    if continent == "oceania":
        continent = "Oceania"
    if continent == "antarctica":
        continent = "Antarctica"

    data = pd.read_csv(file)
    country_code = data['Country code'].tolist()
    for i in range(len(country_code)):
        country_code[i] = str(country_code[i]).replace(',', ' ')
    countries = " ".join(str(i) for i in country_code)
    country_list = countries.split(" ")

    different_country_dictionary_list = []
    different_country = []


    if (len(country_list)>1):
        for k in range(len(country_list)):
            if country_list[k] not in different_country:
                try:
                    continent_of_this_country = country_to_continent(country_list[k])
                except:
                    continue

                if continent_of_this_country == continent:
                    different_country.append(country_list[k])
                    country_dictionary = {'Country': country_list[k], 'Frequency': 1}
                    different_country_dictionary_list.append(country_dictionary)
            else:
                for j in range(len(different_country)):
                    if different_country_dictionary_list[j]['Country'] == country_list[k]:
                        different_country_dictionary_list[j]['Frequency'] = different_country_dictionary_list[j]['Frequency'] + 1

    for i in range(len(different_country_dictionary_list)):
        country_code = different_country_dictionary_list[i]['Country']
        try:
            different_country_dictionary_list[i]['Country'] = pycountry.countries.get(alpha_2=country_code).name
        except:
            continue

    name = ['Country', 'Frequency']
    df = pd.DataFrame(columns=name, data=different_country_dictionary_list)  # 数据有三列，列名分别为one,two,three
    df = df.sort_values(by='Frequency', ascending=False)
    edition = "edition"+edition_num
    dirName = output_dir + "\\" + edition
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    dirName = dirName + "\\" + str(continent) + ".csv"
    df.to_csv(dirName,index=False)



def read_file(edition_num):
    edition_num = str(edition_num)
    dirs = os.listdir(path + edition_num)
    for file in dirs:
        if file != 'output.csv':
            fp1 = path + edition_num + '/' + file
            f = open(fp1, encoding='utf-8')
            print()
            print('filename: ', file)
            a = f.read()
            f.close()
            find_most_mentioned_countries(fp1, edition_num, file)


for i in range(1,9):
    read_file(i)
