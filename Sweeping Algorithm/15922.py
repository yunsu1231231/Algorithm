# 입력 
N = int(input())
arr =[]
for i in range(N):
    A = list(map(int,input().split()))
    arr.append(A)

distance = arr[0][1] - arr[0][0]

# 연산
for i in range(0,len(arr)-1):
    if arr[i][1] > arr[i+1][0] and arr[i+1][1] > arr[i][1]:
        distance += arr[i+1][1] - arr[i][1]
    elif arr[i][0] >= arr[i+1][0] and arr[i+1][1] <= arr[i+1][1]: # 안에 포함
        continue
    else: # 같을 때 
        distance += arr[i+1][1] - arr[i+1][0]

print(distance)