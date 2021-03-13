import sys

input = sys.stdin.readline

def backtracking(depth):
    if depth == M:
        print(' '.join(map(str, printList)))
        return

    for i in range(1, N + 1):
        if depth == 0:
            printList.append(i)
            backtracking(depth + 1)
            printList.pop()
        else:
            if printList[-1] <= i:
                printList.append(i)
                backtracking(depth + 1)
                printList.pop()


N, M = map(int, input().split())

#visited = [False] * (N + 1)
printList = []
backtracking(0)