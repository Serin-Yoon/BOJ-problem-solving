def solution(brown, yellow):
    total = brown + yellow
    multi = []
    yellowMulti = []
    for i in range(1, total + 1):
        if total % i == 0 and i >= (total // i):
            multi.append([i, total // i])

    for i in range(1, yellow + 1):
        if yellow % i == 0 and i >= (yellow // i):
            yellowMulti.append([i, yellow // i])

    print(multi)
    print(yellowMulti)

    for i in range(len(multi)):
        for j in range(len(yellowMulti)):
            if multi[i][0] - yellowMulti[j][0] == 2 and multi[i][1] - yellowMulti[j][1] == 2:
                print(multi[i])
                #return multi[i]


brown, yellow = map(int, input().split())

solution(brown, yellow)