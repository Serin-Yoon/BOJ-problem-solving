import sys

input = sys.stdin.readline

def bs(data):
    start = 0
    end = N - 1
    while (start <= end):
        standard = (start + end) // 2
        if data < numList[standard]:
            end = standard - 1
        elif numList[standard] < data:
            start = standard + 1
        elif numList[standard] == data:
            return 1
    return 0

N = int(input())

numList = sorted(list(map(int, input().split())))

M = int(input())

data = list(map(int, input().split()))

for i in range(M):
    print(bs(data[i]))

