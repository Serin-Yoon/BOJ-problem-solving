S = input()

num = 0
newList = []

for i in range(len(S)):
    if 48 <= ord(S[i]) <= 57:
        num += int(S[i])
    else:
        newList.append(S[i])

newList = sorted(newList, key = lambda x : x)

for i in newList:
    print(i, end='')
print(num)