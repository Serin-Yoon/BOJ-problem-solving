N, M = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0

for i in range(len(data)):
    for j in range(1, len(data) - i):
        if data[i] != data[i + j]:
            cnt += 1

print(cnt)