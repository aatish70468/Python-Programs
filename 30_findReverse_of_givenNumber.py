x = int(input("Enter the number: "))
rev = 0
while x > 0:
    n = x % 10
    rev = (rev * 10) + n
    x = int(x / 10)

print(rev)
