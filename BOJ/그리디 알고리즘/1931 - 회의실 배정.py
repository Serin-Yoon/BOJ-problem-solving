import sys

input = sys.stdin.readline

N = int(input())
list = []

for i in range(N):
    start, end = map(int, input().split())
    list.append([start, end])

list = sorted(list, key=lambda l: l[0])
list = sorted(list, key=lambda l: l[1])

endTime = list[0][1]
cnt = 1

for i in range(1, N):
    if list[i][0] >= endTime:
        endTime = list[i][1]
        cnt += 1

print(cnt)