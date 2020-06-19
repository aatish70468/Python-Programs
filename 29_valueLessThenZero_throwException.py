try:
    x = int(input("Enter the value: "))
    if x < 0:
        throw
    else:
        print("Your entered value is " + str(x))
except Exception:
    print("Your entered value is less then zero")
