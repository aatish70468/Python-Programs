x = int(input("Enter the number: "))
y = x
sum = 0
while x > 0:
    n = x % 10
    sum = sum + (n * n * n)
    x = int(x / 10)

if y == sum:
    print("Number is Amstrong")
else:
    print("Number is not Amstrong")
