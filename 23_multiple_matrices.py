no_row_1 = int(input("Enter the no. of row of 1st matrix: "))
no_column_1 = int(input("Enter the no. of column of 1st matrix: "))

m1 = []
print("Enter the entries rowwise: ")
for i in range(no_row_1):
    a = []
    for j in range(no_column_1):
        a.append(int(input()))
    m1.append(a)
print(m1)
no_row_2 = int(input("Enter the no. of row of 2nd matrix: "))
no_column_2 = int(input("Enter the no. of column of 2nd matrix: "))

m2 = []
print("Enter the entries rowwise: ")
for i in range(no_row_2):
    b = []
    for j in range(no_column_2):
        b.append(int(input()))
    m2.append(b)
print(m2)
m3 = []
for i in range(no_row_1):
    c = []
    for j in range(no_column_2):
        c.append(int(0))
    m3.append(c)
print(m3)
for q in range(no_row_2):
    for w in range(len(m2[0])):
        for j in range(no_row_1):
            a = m1[q][j]
            b = m2[j][w]
            m3[q][w] += (a * b)

print(m3)


