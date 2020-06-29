string = input("Enter the String: ")
print("Iterative")
count_1 = {}
a = 0
for i in string:
    print(i)
    a = string.count(i)
    count_1[i] = a
print(count_1)
print("Recursive")
count_2 = {}
b = 0
def char_count(x):
    if x == -1:
        return count_2
    else:
        j = string[x]
        b = string.count(j)
        count_2[i] = b
        char_count(x-1)
length = len(string)
print(string[length - 1])
count_3 = {}
count_3 = char_count(length - 1)
print(count_3)
