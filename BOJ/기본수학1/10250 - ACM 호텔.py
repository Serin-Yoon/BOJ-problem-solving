
T = int(input())

for i in range(T):
    H, W, N = input().split()
    H = int(H)
    W = int(W)
    N = int(N)

    resH = N % H
    resW = N // H
    if (resH == 0): res = H * 100 + resW
    else: res = resH * 100 + resW + 1

    print(res)
