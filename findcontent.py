import csv
import json
import requests
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import fnmatch
import os
import re
import numpy as np
import librosa
import matplotlib.pyplot as plt
import librosa.display
from sklearn.manifold import TSNE
import json

name_list = []
path = "F:\Edin\研一上\Data Science for Design\Encyclopedia Britannica\Data\encyclopaedia-britannica-sample\part\extensible_markup_language_part"
# output_dir = 'F:\Edin\研一上\Data Science for Design\Encyclopedia Britannica\Data\encyclopaedia-britannica-sample\part\comma_separated_values'
files = []
for root, dirnames, filenames in os.walk(path):
    for filename in fnmatch.filter(filenames, '*.xml'):
        files.append(os.path.join(root, filename))

print("found %d .xml files in %s" % (len(files), path))


def read_file(file):
    with open(file, encoding='UTF-8')as f:
        a = f.read()
    f.close()
    return a

#
# ## below is for extracting the names of the columns
# for i, f in enumerate(files):
#     if i % 1 == 0:
#         print("print %d of %d = %s" % (i + 1, len(files), f))#
#     # 2. 基于文件对象构建 csv写入对象
#     csv_writer = csv.writer(output)
#
#     # 3. 构建列表头
#     name = f
#     if name.endswith('.xml'):
#         name = name[-16:]
#         name_list.append(name)
# ## write the column names as the name of the .xml file
# print(name_list)
# csv_writer.writerow(name_list)

## write the corresponding words inside each column
for i, f in enumerate(files):
    if i % 1 == 0:
        print("write %d of %d = %s" % (i + 1, len(files), f))

    a = read_file(f)
    b = a.split()

    for c in b:
        d = c.split("CONTENT=")
        if len(d) == 1:
            continue
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
        url = url + d[1][1:-1]
        response = requests.get(url)

        name = f
        if name.endswith('.xml'):
            name = name[-16:-4]
            # name_list.append(name)
    ## write the column names as the name of the .xml file
    # print(name_list)

        output = open(name+'.csv', mode='a', encoding='utf-8', newline='')
        csv_writer = csv.writer(output)
        try:
            json_format = response.json()
            if (json_format[0]['word']):
                word = json_format[0]['word']
                if (len(word) != 1):
                    print(word)
                    print(word, file=output)
        except:
            print("not found!")