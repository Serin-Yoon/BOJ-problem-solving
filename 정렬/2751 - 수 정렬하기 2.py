N = int(input())

numList = []

for i in range(N):
    numList.append(int(input()))

#파이썬 내장함수 sorted
numList = sorted(numList)

for i in range(0, N):
    print(numList[i])