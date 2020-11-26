import fnmatch
from geotext import GeoText
import os
import pycountry
import pycountry_convert as pc

path = r"F:\Edin\1_1\Data Science for Design\Encyclopedia Britannica\Data\Test"
# test
files = []
for root, dirnames, filenames in os.walk(path):
    for filename in fnmatch.filter(filenames, '*.txt'):
        files.append(os.path.join(root, filename))

print("found %d .txt files in %s" % (len(files), path))


country_list = []
different_country_code = []
different_country = []
different_continent = []
continent_list = []

def read_file(file):
    with open(file, encoding='UTF-8')as f:
        a = f.read()
    f.close()
    return a


def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_nam = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_nam

for i, f in enumerate(files):
    if i % 10 == 0:
        print("processed the %d  of %d = %s" % (i + 1, len(files), f))

    a = read_file(f)
    b = a.split("\n")

    '''
    process the txt with spaCy, 
    use: python3 -m spacy download en_core_web_sm 
    to download en_core_web_sm
    
    '''
    # nlp = spacy.load("en_core_web_sm")
    # for line in b:
    #     doc = nlp(line)
    #     for ent in doc.ents:
    #         print(ent.text)


    # process the txt with GeoText
    for line in b:
        places = GeoText(line)
        if len(places.cities) != 0:
            # print(places.cities)
            for key in places.country_mentions.keys():
                country_list.append(key)
            for country_code in country_list:
                if country_code not in different_country_code:
                    different_country_code.append(country_code)

    for country_code in different_country_code:
        country = pycountry.countries.get(alpha_2=country_code)
        try:
            different_country.append(country.name)
        except:
            continue


for country in different_country:
    continent = country_to_continent(country)
    continent_list.append(continent)

for continent in continent_list:
    if continent not in different_continent:
        different_continent.append(continent)

print(different_continent)
