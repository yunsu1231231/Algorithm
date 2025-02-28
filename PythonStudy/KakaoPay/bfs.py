# 카페 코테 빈출유형 

from collections import deque # collections 모듈 / deque 클래스 

def bfs(graph,start):
    visited = set()
    queue = deque([start]) # 오버로딩, 인자 없이 + iterable 인자로 가능 
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex) # set일 때는 add 함수 
            print(vertex, end = " ")
            queue.extend(graph[vertex] - visited) # extend 메서드는 인자로 주어진 반복 가능한 객체(여기서는 집합)의 각 요소를 deque의 끝에 차례로 추가
    print()

graph = {1: {2, 3}, 2: {1, 4}, 3: {1, 4}, 4: {2, 3}}
bfs(graph, 1)        
    
# extend는 주어진 반복 가능한 객체의 각 요소를 순차적으로 deque에 추가하는 메서드입니다.
    
# graph는 각 노드의 이웃을 저장하는 딕셔너리로 구성된 그래프, 
# start는 탐색을 시작할 노드
# graph[vertex] -> key를 통해 value를 접근 = 딕셔너리 

# deque는 양쪽 끝에서 요소를 추가하거나 제거
# 스택이나 큐의 기능을 하나의 자료구조에서 모두 구현할 수 있습니다.

# deque의 extend 메서드는 리스트의 extend 메서드와 기능적으로 동일
# deque에서도 extend를 사용하여 iterable의 모든 요소를 deque의 오른쪽 끝에 순차적으로 추가
# append 메서드를 여러 번 호출하는 것과 같은 결과를 더 효율적으로 달성

# 대부분의 경우, 작은 숫자부터 큰 숫자 순으로 추가되는 경향

'''
deque에서 자주 사용되는 메서드들은 다음과 같습니다:

append(x):

deque의 오른쪽 끝에 요소 x를 추가합니다.
appendleft(x):

deque의 왼쪽 끝에 요소 x를 추가합니다.
pop():

deque의 오른쪽 끝에서 요소를 제거하고 그 요소를 반환합니다.
popleft():

deque의 왼쪽 끝에서 요소를 제거하고 그 요소를 반환합니다.
extend(iterable):

주어진 iterable의 모든 요소를 deque의 오른쪽 끝에 추가합니다.
'''