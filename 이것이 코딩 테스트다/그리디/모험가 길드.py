N = int(input())

data = sorted(list(map(int, input().split())))
tmpData = data
tmpData2 = data

#뒤에서부터 그룹 짜기
cnt = 0
while len(tmpData) > 0:
    maxNum = tmpData[-1]
    num = maxNum - (2 * maxNum)
    tmpData = tmpData[:num]
    cnt += 1

#앞에서부터 그룹 짜기
cnt2 = 0
while len(tmpData2) > 0:
    minNum = tmpData2[0]
    tmpData2 = tmpData2[minNum:]
    cnt2 += 1

#값 비교
if cnt > cnt2:
    print('뒤에서부터가 크다')
elif cnt < cnt2:
    print('앞에서부터가 크다')
else:
    print('같다')

print(max(cnt, cnt2))