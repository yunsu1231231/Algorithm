import time

import sys
input = sys.stdin.readline

# 시작 시간
start_time = time.time()

N = int(input())
arr = []

for i in range(N):
    a,b = map(int,input().split())
    arr.append((a,1)) # 시작점
    arr.append((b,-1)) # 끝점 
    
arr.sort()

overlap = 0
max_overlap = 0 

for i in arr:
    overlap += i[1]
    max_overlap = max(max_overlap, overlap)

print(max_overlap)

# 종료 시간
end_time = time.time()

# 실행 시간 출력
print(f"Execution time: {end_time - start_time} seconds")