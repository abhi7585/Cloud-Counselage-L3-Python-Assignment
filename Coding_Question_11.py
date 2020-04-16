def selectionSort(arr):
    i = 0
    n = len(arr)
    while i < n-1:
        minIndex = i
        j = i + 1
        while j < n:
            if arr[j] < arr[minIndex]:
                minIndex = j
            j += 1
        else:
            arr[minIndex], arr[i] = arr[i], arr[minIndex]
        i += 1
    else:
        return arr


arr = list(map(int, input().split()))
print(' '.join(map(str, selectionSort(arr))))
