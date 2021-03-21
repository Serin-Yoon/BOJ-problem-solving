import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

coins = [int(input()) for _ in range(N)]
coins.reverse()

count = 0

for coin in coins:
    if coin <= K and K % coin >= 0:
        num = K // coin
        K -= num * coin
        count += num
    if K == 0:
        print(count)
        break