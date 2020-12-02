import heapq
import os
import pandas as pd

# path = r'/Users/wanfangdu/Desktop/DS4D/projectgit/extracted/edition'
path = r'F:\Edin\1_1\Data Science for Design\Encyclopedia Britannica\Coding\Encyclopaedia-Britannica\extracted\edition'
output_dir = r'F:\Edin\1_1\Data Science for Design\Encyclopedia Britannica\Coding\Encyclopaedia-Britannica\longest'
edition_list = []
continent_list = []
entry_list = []
dic = {'Edition': edition_list, 'Continent': continent_list, 'Entry': entry_list}
df = pd.DataFrame(dic)

def find_max_explain(file, edition_num, continent):
    data = pd.read_csv(file)
    # print(data.head())
    explain = data['Entry'].tolist()
    # print(explan)
    if len(explain) != 0:
        longest = heapq.nlargest(1, explain, key=len)
        edition_list.append(edition_num)
        continent_list.append(continent)
        entry_list.append(longest[0])

        # print("longest start")
        # print(type(longest))
        # longest = ','.join(longest)
        # print(longest)
        # print("longest done")

        # for x in longest:
        #     print(type(x))
        #     print(x)
        # longest = max(explan, key=len)
        # print(longest)# this is to find the longest one, use min() to find the shortest one


def read_file(edition_num):
    edition_num = str(edition_num)
    dirs = os.listdir(path + edition_num)
    for file in dirs:
        fp1 = path + edition_num + '/' + file
        if file != 'output.csv':
            f = open(fp1, encoding='utf-8')
            print()
            print('filename: ', file)
            a = f.read()
            f.close()
            find_max_explain(fp1, edition_num, file)
    return a

for i in range(1,9):
    read_file(i)

df['Edition'] = edition_list
df['Continent'] = continent_list
df['Entry'] = entry_list


dirName = output_dir
if not os.path.exists(dirName):
    os.makedirs(dirName)
dirName = dirName + "\\"

df.to_csv(dirName + "longest.csv", index=False)
