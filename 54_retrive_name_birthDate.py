fo = open("54_file.txt", "r")
x = []
for i in fo:
    x.append(i.split())

print(x)
