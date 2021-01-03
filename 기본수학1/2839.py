N = int(input())
M = N
j = N//5
count5 = 0
isAble = False

if (N % 5 == 0):
    res = j

else:
    for i in range(j):
        if ((N-5) % 3 == 0):
            count5 += 1
            count3 = (N - 5) // 3
            res = count5 + count3
            isAble = True
            N -= 5

        else:
            count5 += 1
            N -= 5

    if (not isAble):
        if (M % 3 == 0):
            res = M // 3
        else:
            res = -1

print(res)