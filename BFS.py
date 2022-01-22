from collections import deque

def bfs(graph, start, visited):
    # deque는 Queue다.
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # Queue가 empty될 때까지 loop
    while queue:
        # Queue에서 element 하나 뽑아서 print
        v = queue.popleft()
        print(v, end = ' ')
        # 아직 방문하지 않은 neighbor node들을 queue에 넣는다.
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 그래프
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

# 각 노드가 방문됐는지 확인하는 리스트
visited = [False] * 9

# BFS 함수 실행
bfs(graph, 1, visited)  