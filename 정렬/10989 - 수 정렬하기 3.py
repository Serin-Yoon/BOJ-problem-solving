import sys

N = int(sys.stdin.readline())

list = [0] * 10001

for i in range(N):
    list[int(sys.stdin.readline())] += 1

for i in range(10001):
    #1개 이상 존재하는 경우 개수만큼 출력
    if list[i] > 0:
        for j in range(list[i]):
            print(i)