import sys

input = sys.stdin.readline

N = int(input()) #전깃줄 개수

total = 0

data = []

for i in range(N):
    a, b = map(int, input().split())
    data.append([a, b])
    if a > total:
        total = a
    if b > total:
        total = b

dp = [1] * total

print('전봇대 칸 수:', total)
print('dp:', dp)
print('data:', data)

for i in range(len(data)):
    for j in range(i):
        print('i:', i, 'j:', j)
        if data[j][0] > data[i][0] and data[j][1] < data[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
            print('체크')

print(min(dp))
