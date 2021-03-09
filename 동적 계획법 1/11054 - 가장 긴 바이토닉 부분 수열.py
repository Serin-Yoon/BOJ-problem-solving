import sys

input = sys.stdin.readline

N = int(input())

seq = list(map(int, input().split()))

print(seq)

tmp = seq[0]
min = 1000
next = -1
data = []
start = 0

while (start < len(seq) - 1):
    print('시작 >>', start, '번째 -', seq[start])
    tmp = seq[start]
    min = 1000
    hasUp = False #상승하는 값 있는 경우
    nextIdx = -1
    for i in range(start + 2, len(seq)):
        diff = seq[i] - tmp
        if min > diff and diff > 0:
            min = diff
            nextIdx = i
            hasUp = True
            data.append()
    if hasUp:
        start = nextIdx
    else:

        break

    #print('다음 >>', nextIdx, '번째 -', seq[nextIdx])
    print()
    #start = nextIdx

