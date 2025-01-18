N, T = map(int,input().split())

arr = []

while N == 0:
    for i in range(N):
        arrs = []
        for j in range(i):
            A = list(map(int,input().split()))
            arrs.append(A)
        arr.append(arrs)

print(arr)