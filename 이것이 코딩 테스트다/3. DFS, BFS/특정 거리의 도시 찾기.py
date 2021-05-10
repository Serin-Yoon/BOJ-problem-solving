N, M, K, X = map(int, input().split())

def BFS(node, depth):
    must_visit = [node]
    visited[node] = True
    depthList = [0] * (N + 1)

    while must_visit:
        depth += 1
        node = must_visit[0]
        del must_visit[0]
        for i in range(1, N + 1):
            if linked[node][i] == 1 and not visited[i]:
                must_visit.append(i)
                visited[i] = True

        for mv in must_visit:
            if depthList[mv] == 0:
                depthList[mv] = depth

    if K not in depthList:
        print(-1)
        return

    for i in range(len(depthList)):
        if depthList[i] == K:
            print(i)
    return

linked = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    linked[a][b] = 1

BFS(X, 0)
