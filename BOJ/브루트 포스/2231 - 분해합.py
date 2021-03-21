#각 자리의 합 구하는 함수
def findDigits(n, total):
    if (n // 10) >= 1:
        temp = n % 10
        total += temp
        n -= temp
        n //= 10
        return findDigits(n, total)

    elif (n // 10) < 1:
        total += n
        return total

N = int(input())

#최소값 초기화
min = 1000000
for i in range(1, N):
    data = findDigits(i, 0) + i
    if (data == N and i <= min):
        min = i

#생성자 없는 경우
if (min == 1000000):
    print("0")
#생성자 있는 경우
else:
    print(min)