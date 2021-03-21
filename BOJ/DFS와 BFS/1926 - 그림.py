# import sys
#
# input = sys.stdin.readline
# #
# # def BFS(node):
# #     visited[node] = True
# #     dataList.append(node)
#
#
#     #return
#
# n, m = map(int, input().split())
#
# visited = [False] * (n * m)
#
# paint = [list(map(int, input().split())) for _ in range(n)]
#
# print(paint)
#
# # for i in range(n * m):
# #     if not visited[i] and data[i] == 1:
# #         dataList = []
# #         BFS(i)

arr = [[1, 2, 3, 3], [3, 7, 5, 3], [3, 5, 4, 1], [1, 5, 4, 6]]
dx=[0,0,-1,-1] #상하좌우
dy=[-1,1,0,0]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            print(arr[testX][testY])