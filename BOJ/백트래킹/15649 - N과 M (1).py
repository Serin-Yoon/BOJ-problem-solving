import sys
input = sys.stdin.readline

def backtracking(depth, N, M):
    #깊이가 M일 때 백트래킹 종료
    if depth == M:
        print(' '.join(map(str, printList))) #배열 요소 str 형태로 나란히 출력
        return
    for i in range(1, N+1):
        #방문하지 않은 노드 탐색
        if not visited[i]:
            printList.append(i)
            visited[i] = True #방문처리
            backtracking(depth+1, N, M)
            visited[i] = False #방문처리 초기화
            printList.pop() #탐색 완료 후 노드 모두 제거

N, M = map(int, input().split())

visited = [False] * (N + 1)
printList = []

backtracking(0, N, M)