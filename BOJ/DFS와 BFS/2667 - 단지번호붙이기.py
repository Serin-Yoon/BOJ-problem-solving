import sys

input = sys.stdin.readline

def DFS(x, y, res):
    res.append(N * x + y)
    visited[x][y] = True
    for i in range(4):
        x2 = x + dx[i]
        y2 = y + dy[i]
        if N > x2 > -1 and N > y2 > -1 and data[x2][y2] == 1 and not visited[x2][y2]:
            DFS(x2, y2, res)

    if res not in total:
        total.append(res)

N = int(input())

data = []

#2차원 배열
for i in range(N):
    tmp = input()
    tmp2 = []
    for j in range(N):
        tmp2.append(int(tmp[j]))
    data.append(tmp2)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[False] * N for _ in range(N)]
total = []

for x in range(N):
    for y in range(N):
        if data[x][y] == 1 and not visited[x][y]:
            DFS(x, y, [])

total = sorted(total, key=lambda x : len(x))

print(len(total))

for i in range(len(total)):
    print(len(total[i]))