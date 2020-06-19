n = int(input("Enter the length of array: "))
x = []
for i in range(n):
    x.append(int(input()))

for i in range(n - 1):
    t = x[i]
    x[i] = x[i+1]
    x[i+1] = t

print("Shifted Array")
print(x)
