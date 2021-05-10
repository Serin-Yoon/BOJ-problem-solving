N, K = map(int, input().split())

tube = [] # 시험관 배열
must_visit = [] #바이러스 담을 배열

for i in range(N):
    tmp = list(map(int, input().split()))
    tube.append(tmp)
    for j in range(N):
        if tube[i][j] > 0:
            # 바이러스 우선 순위, 행, 열, 시간(0초)
            must_visit.append((tube[i][j], i, j, 0))

S, X, Y = map(int, input().split())

# 바이러스 우선 순위대로 정렬
must_visit.sort()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while must_visit:
    virus, x, y, time = must_visit[0]
    del must_visit[0]
    # S초 지난 경우
    if time == S:
        break
    # 상하좌우 전염
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 전염 가능 여부 확인
        if 0 <= nx < N and 0 <= ny < N:
            if tube[nx][ny] == 0:
                tube[nx][ny] = virus
                must_visit.append((tube[nx][ny], nx, ny, time + 1))

print(tube[X - 1][Y - 1])

