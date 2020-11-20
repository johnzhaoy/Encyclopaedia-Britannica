import spacy
from geotext import GeoText
import os


def read_file():
    f = open("./nls-text-encyclopaediaBritannica/193916150.txt", "r")
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
    places = GeoText(line)
    if len(places.cities) != 0:
        print(places.cities)
