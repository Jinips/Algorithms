def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end= ' ')
    # 현재 노드와 연결된 다른 노드를 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 임의의 그래프, index가 node고,
# index에 들어있는 list 정보가 그 node의 neighbor이다.

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

# 각 노드가 방문됐는지 아닌지 확인하는 리스트
visited = [False] * 9

# dfs 함수 실행
dfs(graph, 1, visited)