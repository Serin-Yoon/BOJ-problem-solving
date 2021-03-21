import sys

input = sys.stdin.readline

#깊이 우선 탐색
def DFS(node):
    visited[node] = True #방문처리
    print(node, end=' ')
    for i in range (1, N+1):
        if (graph[node][i] == 1 and not visited[i]):
            DFS(i)

#너비 우선 탐색
def BFS(node):
    must_visit = [node] #탐색해야 할 노드 큐에 추가
    visited[node] = True #방문처리
    while must_visit:
        node = must_visit[0] #맨 처음 노드 탐색
        print(node, end=' ')
        del must_visit[0]
        for i in range (1, N+1):
            if graph[node][i] == 1 and not visited[i]:
                must_visit.append(i) #탐색해야 할 노드 큐에 추가
                visited[i] = True #방문처리

N, M, V = input().split()
N = int(N)
M = int(M)
V = int(V)

graph = [[0]*(N+1) for i in range(N+1)]

for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

visited = [False] * (N + 1)
DFS(V)
print()
visited = [False] * (N + 1)
must_visit = []
BFS(V)