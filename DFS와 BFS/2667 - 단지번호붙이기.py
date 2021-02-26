import sys

input = sys.stdin.readline

N = int(input())
map = []
exist = []
connect = [[False] * (N * N) for i in range(N * N)]


for i in range(N):
    data = input()
    for j in range(N):
        map.append(int(data[j]))

for i in range(N - 1):
    print('i >>', i)
    if i < N * (N - 1):
        if map[i] == 1 and map[i + 7] == 1:
            connect[i][i + 7] = True
            connect[i + 7][i] = True
        if map[i] == 1 and map[i + 1] == 1:
            connect[i][i + 1] = True
            connect[i + 1][i] = True
    else:
        if map[i] == 1 and map[i + 1] == 1:
            connect[i][i + 1] = True
            connect[i + 1][i] = True

for i in range(7):
    print(connect[i])

