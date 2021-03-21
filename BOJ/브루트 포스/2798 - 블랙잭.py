N, M = map(int, input().split())

#N개만큼 카드의 값 입력 받음
cardList = list(map(int, input().split()))

#최대값 초기화
max = 0

for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = cardList[i] + cardList[j] + cardList[k]

            #M보다 작거나 같고 최대값인 경우
            if (total >= max and total <= M):
                max = total

print(max)