import sys

input = sys.stdin.readline

def DFS(depth, curr):
    global num, op, result
    if depth == N - 1:
        result.append(curr)
        return
    if op[0] > 0:
        op[0] -= 1
        DFS(depth + 1, curr + num[depth + 1])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        DFS(depth + 1, curr - num[depth + 1])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        DFS(depth + 1, curr * num[depth + 1])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        if curr < 0:
            DFS(depth + 1, -1 * (abs(curr) // num[depth + 1]))
        else:
            DFS(depth + 1, curr // num[depth + 1])
        op[3] += 1

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
result = []

DFS(0, num[0])
print(max(result))
print(min(result))