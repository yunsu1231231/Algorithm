N,B = map(int,input().split())
hangArray = [] # 이게 이미 행으로 분할 
for i in range(N):
    a = list(map(int,input().split()))
    hangArray.append(a)

# 열 배열 생성 
eulArray = []
for i in range(len(hangArray)): # 0,1
    array_3 = []
    for j in range(len(hangArray)):
        array_3.append(hangArray[j][i]) 
    
    eulArray.append(array_3)

# [[1, 2], [3, 4]]
# [[1, 3], [2, 4]]
    
# 결과 행렬 초기화

resultArray = hangArray  

for i in range(B - 1):  
    Array = []
    for i in range(N):
        row = [0] * N
        Array.append(row)    
    
    # 행렬 곱셈
    for i in range(N):
        for j in range(N):
            for k in range(N):
                Array[i][j] += resultArray[i][k] * eulArray[k][j]

    print(Array)

    resultArray = Array

print(resultArray)

# 열로 전부 분할 

# 1 2    1  2           7  10  1 2           37 54 
# 3 4    3  4           15 22  3 4           81 118

# 88 + 30 = 118 


# 행 * 열 곱 

# 1 2 / 1 3 
# 1 2 / 2 4 


# original = [[1, 2], [3, 4]]


# 0 0 = 0 0 * 0 0 + 0 1 * 1 0
# 0 1 = 0 0 * 0 1 + 
# 1 0 = 1 0   0 0
# 1 1 = 1 0   0 1 

