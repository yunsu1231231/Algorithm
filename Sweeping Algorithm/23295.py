import time

import sys
input = sys.stdin.readline

N, T = int(input.split()) # 참가자 수, 스터디 시간 

arr = []

while N == 0:
    a = list(map(int,input().split()))
    if len(a) == 1: 
        N -= 1
    else: # len(a) == 2
        arr.append(a)    
        


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