N = int(input())

data = sorted(list(map(int, input().split())))

cnt = 0

i = 0
while len(data) > 0:
    if data[i] == 1:
        del data[i]
        cnt += 1