N = int(input())

homes = list(map(int, input().split()))

distance = []

# 안테나 놓을 수 있는 위치 모두 고려
for home in homes:
    tmp = 0
    # 집과 안테나의 거리 계산
    for home2 in homes:
        tmp += abs(home - home2)
    distance.append([home, tmp])

# 거리 오름차순 정렬 후 출력
print(sorted(distance, key = lambda x : x[1])[0][0])