def calculate(cut):
    checkList = []
    for i in range(0, strLen, cut):
        checkList.append(''.join(s[i:i + cut]))
    cntList = []
    for i in range(len(checkList)):
        if i == 0:
            cntList.append([checkList[i], 1])
        else:
            if checkList[i] == cntList[-1][0]:
                cntList[-1][1] += 1
            else:
                cntList.append([checkList[i], 1])
    total = cut * (len(cntList))
    for cnt in cntList:
        if cnt[1] > 1:
            total += len(str(cnt[1]))
    return total

s = input()

strLen = len(s)
totalNum = strLen
answerList = []

for i in range(1, strLen + 1):
    if strLen % i == 0:
        answerList.append(calculate(i))

print(sorted(answerList)[0])