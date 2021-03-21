import sys
import re

input = sys.stdin.readline

#data = input().rstrip('\n')
data = input().rstrip('\n').split('-')
cal = []

for i in range(len(data)):
    num = re.findall('\d+', data[i])
    tmp = 0
    for j in range(len(num)):
        tmp += int(num[j])
    cal.append(tmp)

final = 0
for i in range(len(cal)):
    if i == 0:
        final += cal[i]
    else:
        final -= cal[i]

print(final)
