from itertools import combinations

N = int(input())
coins = sorted(list(map(int, input().split())))

data = []

for i in range(1, N + 1):
    tmpList = list(combinations(coins, i))
    for j in range(len(tmpList)):
        data.append(sum(tmpList[j]))

data = sorted(list(set(data)))

for i in range(1, data[-1]):
    if i not in data:
        print(i)
        break
