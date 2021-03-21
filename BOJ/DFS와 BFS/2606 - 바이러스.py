import sys

input = sys.stdin.readline

def DFS(node):
    visited[node] = True
    for i in range (1, N+1):
        if graph[node][i] == 1 and not visited[i]:
            DFS(i)

N = int(input())
V = int(input())

graph = [[0]*(N+1) for i in range(N+1)]

for i in range(V):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

visited = [False] * (N + 1)

DFS(1)
count = -1
for i in visited:
    if visited[i]:
        count += 1
print(count)