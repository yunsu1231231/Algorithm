A = input()
B = input()

dp = []

for i in range(len(B)+1):
    row = []
    for j in range(len(A)+1):
        row.append(0)
    dp.append(row)

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            dp[j][i] = dp[j-1][i-1] + 1
        else:
            dp[j][i] = max(dp[j-1][i],dp[j][i-1])

print(dp[len(B)][len(A)])