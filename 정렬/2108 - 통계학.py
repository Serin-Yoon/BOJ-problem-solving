from collections import Counter

N = int(input())

numList = []
total = 0

for i in range(N):
    data = int(input())
    numList.append(data)
    total += data

numList.sort()

#산술평균
print(int(round(total/N, 0)))

#중앙값
print(numList[int((N + 1)/2 - 1)])

#최빈값
if (N > 1):
    cnt = Counter(numList)
    cnt_sort = cnt.most_common(2)
    if cnt_sort[0][1] == cnt_sort[1][1]:
        print (cnt_sort[1][0])
    else:
        print (cnt_sort[0][0])
elif (N == 1):
    print(numList[0])

#범위
max = -4000
min = 4000

for i in range(N):
    if numList[i] >= max:
        max = numList[i]
    if numList[i] <= min:
        min = numList[i]

print(max - min)
