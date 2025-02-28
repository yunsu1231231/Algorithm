def rotate_matrix(mat):
    n = len(mat)
    for i in range(n // 2):
        for j in range(i,n-i-1):
            temp = mat[i][j]
            mat[i][j] = mat[n-1-j][i] # 첫 번째 원소
            mat[n-1-j][i] = mat[n-1-i][n-1-j] # 왼쪽 열의 맨 아래 원소 자리 <- 아래쪽 행의 맨 오른쪽 원소
            mat[n-1-i][n-1-j] = mat[j][n-1-i] # 아래쪽 행의 맨 오른쪽 원소 자리 <- 오른쪽 열의 맨 위 원소를 저장
            mat[j][n-1-i] = temp # 오른쪽 열의 맨 위 원소 자리 <- temp에 저장해 둔 첫 번째 원소
    return mat

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate_matrix(matrix)
print(matrix)
            
# mat을 시계 방향으로 90도 회전하는 함수 rotate_matrix를 구현한 것
# 회전하는 네개의 꼭짓점만 변화 


# 이중 for문 -> 각 레이어를 회전하는 역할 

# i 값이 layer
# i부터 n-i-1 까지 -> 마지막은 중복으로 처리되므로 빼준다 
