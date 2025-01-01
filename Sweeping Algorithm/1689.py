import time

import sys
input = sys.stdin.readline

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

