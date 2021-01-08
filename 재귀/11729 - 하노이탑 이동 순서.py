# 1) N-1개의 원판을 1번에서 2번으로 옮김
# 2) 맨밑 원판을 1번에서 3번으로 옮김
# 3) N-1개의 원판을 2번에서 3번으로 옮김

N = int(input())

#총 이동횟수 계산 함수
def total(N):
    if (N == 1):
        output = 1
    else:
        output = total(N-1) + 2**(N-1)
    return output

#이동 과정 출력 함수
def process(N, a, b, c):
    if (N == 1):
        print(a, c)
    else:
        process(N-1, a, c, b) #N-1개를 a에서 b로 옮김
        print(a, c) #맨밑 원판을 a에서 c로 옮김
        process(N-1, b, a, c) #N-1개를 b에서 c로 옮김

ans = total(N)
print(ans)
process(N, 1, 2, 3)