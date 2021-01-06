M, N = map(int, input().split())

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
    for i in range(a, b+1):
        #1보다 크고 True인 값만 출력
        if i > 1 and prime[i] == True:
            print(i)

isPrime(M, N)
