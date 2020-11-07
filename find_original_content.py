def read_file():
    f = open("./alto/188082735.34.xml", "r")
    a = f.read()
    f.close()
    return a


a = read_file()
# b = a.split("\n")
b = a.split()

output = open('content_output.csv', mode='a', encoding='utf-8')

for c in b:
    d = c.split("CONTENT=")
    if len(d) == 1:
        continue
    print(d[1][1:-1])
    print(d[1][1:-1], file=output)

