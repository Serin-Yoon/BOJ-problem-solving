S = list(map(int, input()))

cnt1 = 0
cnt2 = 0

#0을 뒤집는 경우 & 1을 뒤집는 경우
for i in range(len(S) - 1):
    if S[i] == 0 and S[i + 1] == 1:
        cnt1 += 1
    if S[i] == 1 and S[i + 1] == 0:
        cnt2 += 1
if S[-1] == 0:
    cnt1 += 1
else:
    cnt2 += 1

print(min(cnt1, cnt2))