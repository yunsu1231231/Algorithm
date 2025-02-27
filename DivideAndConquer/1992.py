n = int(input())  

# 영상 입력
image = []
for i in range(n):
    row = list(input())  
    image.append(row)  


# 시작 위치, 크기 
x, y, size = 0, 0, n
stack = [(x, y, size)]  

# 저장 문자열 
result = ""  

while stack:
    x, y, size = stack.pop()

    firstValue = image[x][y]  
    isSame = True

    # 값 일치여부 확인 
    for i in range(x, x + size):
        for j in range(y, y + size):
            if image[i][j] != firstValue:
                isSame = False
                break
        if not isSame:
            break

    # 모두 같으면 
    if isSame:
        result += firstValue
    else:
        result += "("
        halfSize = size // 2
        # 4개의 구역으로 나누어 재귀적으로 처리
        stack.append((x + halfSize, y + halfSize, halfSize))
        stack.append((x + halfSize, y, halfSize))
        stack.append((x, y + halfSize, halfSize))
        stack.append((x, y, halfSize))
        result += ")"

print(result)


