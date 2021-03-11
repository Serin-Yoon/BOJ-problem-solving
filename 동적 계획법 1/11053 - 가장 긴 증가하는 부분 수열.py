import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))