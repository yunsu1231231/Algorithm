import heapq

arr = []
N = int(input())
for i in range(N):
    A = list(map(int,input().split()))
    arr.append(A)
arr.sort()

heap = []

# 초기값 
heapq.heappush(heap,arr[0][1])

for i in arr[1:]:
    start = i[0]
    end = heap[0]
    
    if start >= end:
        heapq.heappop(heap)
    
    heapq.heappush(heap,i[1])

print(len(heap))