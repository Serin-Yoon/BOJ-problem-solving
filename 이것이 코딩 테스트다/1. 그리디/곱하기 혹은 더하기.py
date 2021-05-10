S = input()

data = 0

for i in range(len(S)):
    if int(S[i]) != 0:
        if data == 0:
            data += int(S[i])
        else:
            data *= int(S[i])

print(data)