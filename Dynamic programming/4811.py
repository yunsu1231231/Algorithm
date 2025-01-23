def aahh(n):
    dp = [[0] * (n + 1) for i in range(2 * n + 1)]
    
    # dp = []
    # for i in range(2* n+1):
    #    dp.append([0] * (n+1))
    
    dp[0][0] = 1

# i 전체, j 약 반개 
    for i in range(2 * n): 
        for j in range(n + 1):
            if dp[i][j] > 0:
                if j < n:
                    dp[i + 1][j + 1] += dp[i][j] # W를 꺼낸 경우
                if j > 0:
                    dp[i + 1][j - 1] += dp[i][j] # H를 꺼낸 경우

    return dp[2 * n][0]

while True:
    n = int(input())
    if n == 0:
        break
    print(aahh(n))




# NameError는 파이썬에서 발생하는 예외 중 하나로, 정의되지 않은 변수나 이름을 사용할 때 발생

# IndexError는 파이썬에서 발생하는 예외 중 하나로, 
# 리스트, 튜플, 문자열 등과 같은 시퀀스 타입에서 유효하지 않은 인덱스를 참조할 때 발생하는 오류

# Traceback은 파이썬에서 오류가 발생한 위치와 호출 스택(call stack)을 보여주는 메시지

# Traceback 메시지는 두 가지 중요한 정보를 제공
# 1. 실행 시점에서의 문제 (호출 스택):
# 2. 그 아래 부분은 실제로 오류가 발생한 코드와 관련된 상세 정보를 제공

# n = 3
# result = [0] * (n + 1)
# print(result) # [0, 0, 0, 0]
# 리스트의 복사본을 만들고, 모든 요소가 동일한 값  

# dp(i, j) = dp(i-1, j+1) + dp(i, j-1) 

# 의존관계 A가 B에 의존한다 / B가 바뀌면 A가 바뀐다
# i가 바뀌면 j가 바뀐다 -> j가 i에 의존한다 

# j가 i에 의존하기 때문에, i가 바깥쪽 반복문이고, j가 안쪽 반복문인 형태로 for문을 작성