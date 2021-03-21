import sys

input = sys.stdin.readline

N, M = map(int, input().split())

map = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    tmp = input()
    tmp2 = []
    for j in range(M):
        tmp2.append(int(tmp[j]))
    map.append(tmp2)

queue = [[0, 0]]
map[0][0] = 1

while queue:
    x = queue[0][0]
    y = queue[0][1]
    del queue[0]
    for i in range(4):
        x2 = x + dx[i]
        y2 = y + dy[i]
        if -1 < x2 < N and -1 < y2 < M and map[x2][y2] == 1:
            queue.append([x2, y2])
            map[x2][y2] = map[x][y] + 1

print(map[N-1][M-1])