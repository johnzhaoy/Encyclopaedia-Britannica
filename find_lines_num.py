import os

dirs = os.listdir(r'./alto')

for file_path in dirs:
    count = 0
    # print("file: ", file_path)
    file_path2 = './alto/' + file_path
    # print(file_path2)
    with open(file_path2, encoding='UTF-8')as f:
        a = f.read()
    f.close()

    b = a.split()

    for c in b:
        if (c == '</TextLine>') or (c == 'STYLEREFS="font0"/></TextLine><TextLine'):
            count = count + 1
    print(file_path, ',', count)

    output = open('lines_num_output.csv', mode='a', encoding='utf-8')
    print(file_path, ',', count, file=output)
