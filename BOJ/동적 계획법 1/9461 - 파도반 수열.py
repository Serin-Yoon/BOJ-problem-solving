import sys

input = sys.stdin.readline


def P(N):
    if N < 4:
        return 1
    elif N < 6:
        return 2
    if dp[N]:
        return dp[N]
    dp[N] = P(N-1) + P(N-5)
    return dp[N]


T = int(input())

for i in range(T):
    dp = [0] * 101
    N = int(input())
    print(P(N))
