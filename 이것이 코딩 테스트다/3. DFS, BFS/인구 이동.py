N, L, R = map(int, input().split())

population = [[0] * N for _ in range(N)]

for r in range(N):
    tmp = list(map(int, input().split()))
    for c in range(N):
        population[r][c] = tmp[c]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

must_visit = [[0, 0]]
visited = [[False] * N for _ in range(N)]
day = 0
total = []

while day == 0 or len(total) > 0:
    day += 1
    while must_visit:
        x, y = must_visit[0]
        visited[x][y] = True
        if must_visit[0] not in total:
            total.append(must_visit[0])
        del must_visit[0]

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동 가능 여부 확인
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                pop1 = population[x][y]
                pop2 = population[nx][ny]

                if L <= abs(pop1 - pop2) <= R:
                    must_visit.append([nx, ny])

    cal = 0

    for xy in total:
        cal += population[xy[0]][xy[1]]

    for xy in total:
        population[xy[0]][xy[1]] = cal // len(total)

    print(population[0])
    print(population[1])
    print(population[2])

    total = []

