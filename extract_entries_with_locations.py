import spacy
from geotext import GeoText
import os


def read_file():
    # f = open(r"F:\Edin\1_1\Data Science for Design\Encyclopedia Britannica\Data\Raw\nls-text-encyclopaediaBritannica\193819047.txt", "r", encoding='UTF-8')
    f = open("/Users/wanfangdu/Desktop/DS4D/Project/nls-text-encyclopaediaBritannica/194167545.txt", "r")
    a = f.read()
    f.close()
    return a


a = read_file()
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
    words = line.split(" ")
    for word in words:
        if (word.isupper() is True) and (len(word)>3 and word != 'VIII.'):
            # I wanna make it doesn't include rome numbers but cannot find a better way
            print('---------')
            print(word)
    places = GeoText(line)
    if len(places.cities) != 0:
        print(places.cities)
