import array
print("Linear Search")
def linearSearch(arr_linear, length, find_value):
    for i in range(length):
        if arr_linear[i] == find_value:
            return i
    return -1

n = int(input("Enter the number of elements: "))
arr_linear = array.array("u")
for i in range(n):
    arr_linear.append(input("Enter the number: "))

#arr_linear = sorted(arr_linear)
x = input("Enter the number you wan't to found: ")
result = linearSearch(arr_linear, len(arr_linear), x)
if result != -1:
    print("Element present at index " + str(result))
else:
    print("Element not found")


print("Binary Search")
def binarySearch(arr_binary, start, end, find_value):
    if end >= start:
        mid = int((start+end)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr_binary, start, mid-1, x)
        else:
            return binarySearch(arr_binary, mid+1, end, x)
    else:
        return -1

n = int(input("Enter the number of elements: "))
arr_binary = array.array("u")
for i in range(n):
    arr_binary.append(input("Enter the number: "))

arr_binary = sorted(arr_binary)
x = input("Enter the number you wan't to found: ")
result = binarySearch(arr_binary, 0, len(arr_binary)-1, x)
if result != -1:
    print("Element present at index " + str(result))
else:
    print("Element not found")
