import sys

input = sys.stdin.readline


def backtracking(depth, N, M):
    #깊이가 M일 때 백트래킹 종료
    if depth == M:
        print(' '.join(map(str, printList)))
        return
    for i in range(1, N + 1):
        if depth == 0:
            printList.append(i)
            backtracking(depth + 1, N, M)
            printList.pop()
        else:
            if printList[-1] <= i:
                printList.append(i)
                backtracking(depth + 1, N, M)
                printList.pop()


N, M = map(int, input().split())

visited = [False] * (N + 1)
printList = []

backtracking(0, N, M)
