def binary_search(arr,target):
    left, right = 0, len(arr) - 1 
    while left <= right:
        mid = (left + right) // 2 
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 # 배열 전체를 검색했지만 타겟 값과 일치하는 요소를 찾지 못했음

arr = [1,2,3,4,5,6,7,8,9]
target = 4 
print(binary_search(arr,target))

