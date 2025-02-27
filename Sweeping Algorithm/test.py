N = map(int,input().split())


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = int(len(arr) / 4)
    
    left = arr[:mid]
    right = arr[mid:]
    left_sorted = mergeSort(left)
    right_sorted = mergeSort(right)
    
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

for _ in mergeSort(chicken):
    print(_, end = " ")