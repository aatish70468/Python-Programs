def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    print(str(n1) + " " + str(n2))
    #create arrays
    Left = [0] * (n1)
    Right = [0] * (n2)
    #copy data to arrays
    for i in range(0, n1):
        Left[i] = arr[l + i]
    print(Left)
    for j in range(0, n2):
        Right[j] = arr[m + 1 + j]
    print(Right)
    i = 0 #first half of array
    j = 0 #second half of array
    k = l #merges two halves
    while i<n1 and j<n2:
        if Left[i]<=Right[j]:
            arr[k] = Left[i]
            i += 1
        else:
            arr[k] = Right[j]
            j += 1
        k += 1
    #copy the left out elements of left half
    while i<n1:
        arr[k] = Left[i]
        i += 1
        k += 1
    #copy the left out elements of right half
    while j<n2:
        arr[k] = Right[j]
        j += 1
        k += 1
    print(arr)

def mergeSort(arr, l, r):
    if l<r:
        #getting the mid value
        mid = (l+(r-1))//2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, r)
        merge(arr, l, mid, r)

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
mergeSort(arr, 0, n-1)
print("Sorted Array: ")
for i in range(n):
    print(arr[i], end = " ")


