import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

data.reverse()
dp2 = [0] * N

for i in range(N):
    for j in range(i):
        if data[j] < data[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp2.reverse()
dp3 = []

for i in range(N):
    dp3.append(dp[i] + dp2[i])

print(max(dp3))