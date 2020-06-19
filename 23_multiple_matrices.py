no_row_1 = int(input("Enter the no. of row of 1st matrix: "))
no_column_1 = int(input("Enter the no. of column of 1st matrix: "))

m1 = []
print("Enter the entries rowwise: ")
for i in range(no_row_1):
    a = []
    for j in range(no_column_1):
        a.append(int(input()))
    m1.append(a)

no_row_2 = int(input("Enter the no. of row of 2nd matrix: "))
no_column_2 = int(input("Enter the no. of column of 2nd matrix: "))

m2 = []
print("Enter the entries rowwise: ")
for i in range(no_row_2):
    b = []
    for j in range(no_column_2):
        b.append(int(input()))
    m2.append(b)

m3 = []
for i in range(no_row_2):
    c = []
    for j in range(no_column_1):
        c.append(int(0))
    m3.append(c)

for q in range(no_row_1):
    for w in range(m2[0]):
        for j in range(no_column_1):
            a = m1[q][j]
            b = m2[j][q]
            m3[q][j] += a * b

    
    
        
print(m1)
print(m2)
print(m3)


