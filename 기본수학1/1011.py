T = int(input())

for i in range(T):
    x, y = input().split()
    x = int(x)
    y = int(y)
    length = y-x

    j = 1
    while (True):
        if ((j-1)*j < length and length <= j*j):
            res = j*2 - 1
            break
        elif (j*j < length and length <= j*(j+1)):
            res = j*2
            break
        else: j += 1

    print(res)
