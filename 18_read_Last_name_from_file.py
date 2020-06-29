fo = open("18_file_1.txt", "r")
array = []
for i in fo:
    array.append(i.split())

lastName = []
for j in range(len(array)):
    lastName.append(array[j][2])

fo.close()
print("Sorted Last Name: ")
fo = open("18_file_2.txt", "w")
for i in range(len(lastName)):
    fo.write(lastName[i] + "\n")
    
lastName.sort()
print(lastName)
fo.close()
