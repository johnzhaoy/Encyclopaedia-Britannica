import heapq
import os
import pandas as pd

path = r'/Users/wanfangdu/Desktop/DS4D/projectgit/extracted/edition'


def find_max_explan(file):
    data = pd.read_csv(file)
    # print(data.head())
    explan = data['Entry'].tolist()
    # print(explan)
    if len(explan) != 0:
        twolongest = heapq.nlargest(9, explan, key=len)
        for x in twolongest:
            print(x)
        # longest = max(explan, key=len)
        # print(longest)# this is to find the longest one, use min() to find the shortest one


def read_file(edition_num):
    dirs = os.listdir(path + edition_num)
    for file in dirs:
        fp1 = path + edition_num + '/' + file
        if file != 'output.csv':
            f = open(fp1, encoding='utf-8')
            print()
            print('filename: ', file)
            a = f.read()
            f.close()
            find_max_explan(fp1)
    return a

read_file('6')


