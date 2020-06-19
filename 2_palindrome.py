def palindrom(x):
    i = 0
    while x > 0:
        a = x % 10
        i = i * 10 + a
        x = int(x / 10)
    return i

x = int(input("Enter the number: "))
num = int(x)
rev = int(palindrom(x))
if num == rev:
    print("Entered number is palindrom.")
else:
    print("Entered number is not palindrom.")
