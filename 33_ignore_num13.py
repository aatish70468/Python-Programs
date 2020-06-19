n = int(input("Enter the length of array: "))
x = []
print("Enter the value having at least one 13 value: ")
for i in range(n):
    x.append(int(input()))

sum = 0
for i in range(n):
    if x[i] != 13:
        sum = sum + x[i]

print("Sum of array: " + str(sum))
