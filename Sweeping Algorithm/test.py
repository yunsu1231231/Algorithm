def aahh(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]  # DP 테이블 초기화

    dp[0][0] = 1  # 초기 상태: 0개의 약이 남았을 때, 0개의 W와 H가 출력됨

    for i in range(n):  # 약을 i번 꺼낸 상태에서
        for j in range(i + 1):  # j번 W가 나온 상태에서
            if dp[i][j] > 0:
                dp[i + 1][j + 1] += dp[i][j]  # W를 꺼낸 경우
                dp[i + 1][j] += dp[i][j]  # H를 꺼낸 경우

    return dp[n][0]  # n번 약을 다 썼을 때, H만 남은 경우의 개수

while True:
    n = int(input())  # N 값 입력 받기
    if n == 0:  # 0이 입력되면 종료
        break
    print(aahh(n))  # 계산된 결과 출력
