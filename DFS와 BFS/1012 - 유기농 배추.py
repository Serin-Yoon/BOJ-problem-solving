import sys

input = sys.stdin.readline

def DFS(x, y, res):
    res.append([x, y])
    visited[x][y] = True

    for i in range(4):
        x2 = x + dx[i]
        y2 = y + dy[i]
        if -1 < x2 < N and -1 < y2 < M and not visited[x2][y2] and cabbage[x2][y2] == 1:
            DFS(x2, y2, res)

    if res not in total:
        total.append(res)

T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())

    #M은 가로(열) N은 세로(행)
    cabbage = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    total = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(K):
        X, Y = map(int, input().split())
        #X는 y값 Y는 x값
        cabbage[Y][X] = 1

    for x in range(N):
        for y in range(M):
            if cabbage[x][y] == 1 and not visited[x][y]:
                DFS(x, y, [])

    print(len(total))