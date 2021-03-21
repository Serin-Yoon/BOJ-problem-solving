#소수 출력 함수
def isPrime(a, b):
    #0~b 리스트 생성, True로 초기화
    prime = [True] * (b+1)
    #2부터 루트b까지 실행
    for i in range(2, int(b**0.5)+1):
        if prime[i]:
            #i의 2배수부터 b까지 i의 배수 모두 False로 전환
            for j in range(2*i, b+1, i):
                prime[j] = False

    #여러 케이스 존재하는 경우 두 수의 차이가 가장 적은 것을 출력하기 위해 초기 설정
    diff = 10000
    one = 0
    two = 0

    for i in range(2, b-2+1):

        #두 수 모두 소수인 경우
        if prime[i] == True and prime[b-i] == True:
            if i > b-i:
                tmp = i - (b-i) #두 수의 차이 계산
                if (tmp <= diff):
                    diff = tmp
                    one = b-i
                    two = i
            else:
                tmp = (b-i) - i #두 수의 차이 계산
                if (tmp <= diff):
                    diff = tmp
                    one = i
                    two = b-i
    print(one, two)


T = int(input())

for i in range(T):
    n = int(input())
    isPrime(1, n)
