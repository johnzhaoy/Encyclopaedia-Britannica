import os
import re

dirs = os.listdir(r'./alto')

symbolist = []

# find each file in the folder
for file_path in dirs:
    count = 0
    file_path2 = './alto/' + file_path

    # open the file
    with open(file_path2, encoding='UTF-8')as f:
        a = f.read()
    f.close()

    # split the file with space and store it in a list
    b = a.split()
    list1 = []

    # find the specific attribute
    for c in b:
        d = c.split("CONTENT=")
        if len(d) == 1:
            continue
        list1.append(d[1][1:-1])
    list2 = ''.join(list(list1))
    sub_str = re.sub(u'[a-zA-Z0-9]', '', list2)
    symbolist.append(sub_str)
symbolist2 = ''.join(list(symbolist))
print(symbolist2)

joined = list(symbolist2)

# Create a list to record how many kinds of symbol
each_kind = []

for i in symbolist2:
    if i not in each_kind:
        each_kind.append(i)

# Use a dictionary to record the frequency of each symbol by traversing the list
d = {}

for i in each_kind:
    d[i] = joined.count(i)

for i, j in d.items():
    print(i, ',', j)

    output = open('symbol_num_output.csv', mode='a', encoding='utf-8')
    print(i, ',', j, file=output)

