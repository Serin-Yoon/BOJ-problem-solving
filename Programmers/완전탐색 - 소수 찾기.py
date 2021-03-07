from itertools import permutations

numbers = input()

def solution(numbers):
    totalList = []

    for i in range(0, len(numbers)):
        numList = list(map(int, map(''.join, permutations(list(numbers), i + 1))))
        totalList += numList

    totalList = list(set(totalList))
    return check(totalList)

def check(totalList):
    res = []
    for i in range(len(totalList)):
        data = totalList[i]
        cnt = 0
        for j in range(2, data):
            if data % j == 0:
                cnt += 1
                break
        if data > 1 and cnt == 0:
            res.append(data)
    return len(res)

solution(numbers)