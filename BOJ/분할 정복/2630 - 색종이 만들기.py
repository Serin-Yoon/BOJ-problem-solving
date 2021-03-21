import sys

input = sys.stdin.readline

def count(N, x, y):
    standard = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] != standard:
                count(N // 2, x, y)
                count(N // 2, x, y + N // 2)
                count(N // 2, x + N // 2, y)
                count(N // 2, x + N // 2, y + N // 2)
                return
    total.append(standard)

N = int(input())

paper = []
for i in range(N):
    data = list(map(int, input().split()))
    paper.append(data)

total = []

count(N, 0, 0)

print(total.count(0))
print(total.count(1))