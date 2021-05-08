from itertools import combinations

N, M = map(int, input().split())

def cal(home, chicken):
    total = 0
    for a in home:
        tmp = []
        for b in chicken:
            row = max(a[0], b[0]) - min(a[0], b[0])
            col = max(a[1], b[1]) - min(a[1], b[1])
            tmp.append(row + col)
        total += min(tmp)
    return total

city = []
for i in range(N):
    city.append(list(map(int, input().split())))

home = []
chicken = []

# 집, 치킨집 위치 확인
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append([i, j])
        elif city[i][j] == 1:
            home.append([i, j])

randList = list(combinations(chicken, M))
data = []

for i in range(len(randList)):
    data.append(cal(home, randList[i]))

print(min(data))