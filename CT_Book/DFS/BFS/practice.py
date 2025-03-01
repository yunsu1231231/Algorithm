# https://pythontutor.com/render.html#mode=display

# 재귀 함수가 계속해서 스택에 쌓이는 이유는 
# 각 함수 호출이 완료되기 전까지는 그 결과가 결정되지 않기 때문
# 기저 조건에서 실제 값이 반환되기 시작하면, 각각의 호출이 완료된 것으로 간주
'''
def factorial_interactive(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result 

def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n * n-1
    return n * factorial_recursive(n-1)

print(factorial_recursive(5))
print(factorial_interactive(5))

# 그래프를 표현하는 크게 두 가지 방식 = 인접리스트, 인접행렬 / 가중치 존재 

# 인접행렬 / 행,렬 0 1 2 -> 노드 / 그 안에 값 -> 간선 
# 리스트로 구현 
INF = 99999999

graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

print(graph)

# 인접리스트 -> 2차원 리스트로 구현 
graph_2 = [[] for i in range(3)]

print(graph_2)

# 노드 0에 연결된 노드 정보 저장 (노드,거리)
graph_2[0].append((1,7))

# 노드 1에 연결된 노드 정보 저장
graph_2[1].append((0,7))

graph_2[2].append((0,5))

print(graph_2)
'''

'''
# DFS / 간선 가중치가 존재 x 
def dfs(graph,v,visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
        
    

# 2차원 리스트 <-> 연결정보만, 가중치 x  
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 1차원 리스트
visited = [False] * 9

dfs(graph,1,visited) # 1 = 시작노드 
'''

'''
# 깊이 우선 탐색 
from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = '')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph,1,visited)
'''