def solution(n, vertex):
    visited = [False] * (n + 1)
    queue = [1]
    visited[1] = True
    lastNode = 0

    while queue:
        exist = False
        node = queue[0]
        visited[node] = True
        del queue[0]

        for i in range(1, n + 1):
            if ([node, i] in vertex or [i, node] in vertex) and not visited[i]:
                queue.append(i)
                visited[i] = True
                exist = True
        if not exist:
            lastNode += 1

    print(lastNode)

n = 4

vertex = [[1, 2], [2, 3], [3, 4]]

solution(n, vertex)