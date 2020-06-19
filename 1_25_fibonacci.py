def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

x = int(input("Enter the number: "))
for i in range(x):
    print(fibonacci(i))
