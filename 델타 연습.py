import sys

input = sys.stdin.readline

n = int(input())

paint = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

print(paint)

while True:
    print('행 index >>', end=' ')
    x = int(input())
    print('열 index >>', end=' ')
    y = int(input())
    for i in range(4):
        pointX = x + dx[i]
        pointY = y + dy[i]
        print(paint[pointX][pointY])