import sys

input = sys.stdin.readline

N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

total = 0
i = 0
min = price[0]

while i < N - 1:
    if price[i] < min:
        min = price[i]
    total += (min * length[i])
    i += 1

print(total)