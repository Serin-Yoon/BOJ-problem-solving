import sys

input = sys.stdin.readline

def paint(start, changeNum):
    paint1 = 0
    paint2 = 0
    visited[start] = True

    for i in range(start, start + (7*M)+1, M):
        for j in range(i, i+8):
            if ((i - start) // M) % 2 == 0:
                if (j - i) % 2 == 0:
                    if board[j] == 'B':
                        paint1 += 1
                    else:
                        paint2 += 1
                else:
                    if board[j] == 'B':
                        paint2 += 1
                    else:
                        paint1 += 1
            else:
                if (j - i) % 2 == 0:
                    if board[j] == 'B':
                        paint2 += 1
                    else:
                        paint1 += 1
                else:
                    if board[j] == 'B':
                        paint1 += 1
                    else:
                        paint2 += 1

    if paint1 >= paint2:
        changeNum.append(paint2)
    else:
        changeNum.append(paint1)

    end1 = start + 7
    end2 = start + 7 * M
    while (end1 > M):
        end1 -= M
    while end2 % M != 0:
        end2 -= 1

    if M - end1 > 1 and not visited[start + 1]:
        paint(start + 1, changeNum)
    if N - (end2 // M) > 1 and not visited[start + M]:
        paint(start + M, changeNum)

    return changeNum

N, M = map(int, input().split())

board = []
visited = [False] * (M * N - 1)
changeNum = []

for i in range(N):
    data = input()
    for j in range(M):
        board.append(data[j])

print(sorted(paint(0, changeNum))[0])