N = int(input())

x = []
y = []
rank = []

for i in range(N):
    A, B = map(int, input().split())
    x.append(A)
    y.append(B)
    rank.append(1)

for i in range(0, N):
    for j in range(i+1, N):
        #i번째 사람이 j번째 사람보다 덩치 큰 경우
        if x[i] > x[j] and y[i] > y[j]:
            rank[j] += 1
        #j번째 사람이 i번째 사람보다 덩치 큰 경우
        elif x[i] < x[j] and y[i] < y[j]:
            rank[i] += 1

for i in range(0, N):
    #한줄로 리스트 모든 요소 출력
    print(rank[i], end = ' ')