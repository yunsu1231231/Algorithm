H, W = map(int, input().split())  
A = list(map(int, input().split())) 

array = []

for i in range(len(A)):
    if A[i] != 0: 
        max_value = A[i]  
        for j in range(i, len(A)):  
            if A[i] >= A[j]:  
                array.append(j)  
                max_value = A[j] 
        break 


# 1.범위에 대한 구분 -> 어떻게 범위를 구분? 
# 2.차에 대한 생각 
# 더 적은값을 셀 수 있고 + 자기보다 같거나 큰 값이 나오면 -> 거기서 영역이 나뉜다고 생각



