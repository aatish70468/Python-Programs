"""n = int(input("Enter the number: "))
mul = 1
for i in range(1,n+1):
    print(str(i))
    mul = mul * i
print("Factorial of " + str(n) + ": " + str(mul))"""


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

n = int(input("Enter the number: "))
fac = int(factorial(n))
print("Factorial of " + str(n) + ": " + str(fac))
