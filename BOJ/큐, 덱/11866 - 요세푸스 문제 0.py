import sys

input = sys.stdin.readline

N, K = map(int, input().split())

deque = []

for i in range(1, N + 1):
    deque.append(i)

visited = [False] * (N + 1)
myList = []
ptr = -1

while len(myList) < N:
    if ptr >= N:
        ptr -= N
    for i in range(K):
        ptr += 1
        if ptr >= N:
            ptr -= N

        while visited[ptr]:
            ptr += 1
            if ptr >= N:
                ptr -= N

    visited[ptr] = True
    myList.append(deque[ptr])

print('<', end='')
for i in range(len(myList)):
    if (i < len(myList) - 1):
        print(myList[i], end=', ')
    else:
        print(myList[i], end='')
print('>')