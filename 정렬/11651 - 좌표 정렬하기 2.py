import sys
input = sys.stdin.readline

N = int(input())

location = []

for i in range(N):
    A, B = map(int, input().split())
    location.append([A, B])

#y좌표 기준으로 오름차순 정렬
location.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(location[i][0], location[i][1])
