import sys
input = sys.stdin.readline

N = int(input())

location = []

for i in range(N):
    A, B = map(int, input().split())
    location.append([A, B])

#오름차순 정렬
location = sorted(location)

for i in range(N):
    print(location[i][0], location[i][1])