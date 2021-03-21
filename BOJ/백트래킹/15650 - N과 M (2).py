import sys
input = sys.stdin.readline

def backtracking(depth, N, M):
    #깊이가 M일 때 백트래킹 종료
    if depth == M:
        print(' '.join(map(str, printList)))
        return
    for i in range(1, N+1):
        #방문하지 않은 노드
        if not visited[i]:
            #출력리스트 비어있는 경우 바로 탐색
            if depth == 0:
                printList.append(i)
                visited[i] = True
                backtracking(depth+1, N, M)
                visited[i] = False
                printList.pop()
            else:
                #이전 노드보다 큰 값인 경우 탐색
                if printList[-1] < i:
                    printList.append(i)
                    visited[i] = True
                    backtracking(depth + 1, N, M)
                    visited[i] = False
                    printList.pop()

N, M = map(int, input().split())

visited = [False] * (N + 1)
printList = []

backtracking(0, N, M)