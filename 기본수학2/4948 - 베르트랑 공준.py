N = int(input())

#소수 개수 구하는 함수
def isPrime(a, b):
    total = 0 #소수 개수 초기화
    prime = [True] * (b+1) #0~b 리스트 생성, True로 초기화
    #2부터 루트b까지 실행
    for i in range(2, int(b**0.5)+1):
        if prime[i]:
            #i의 2배수부터 b까지 i의 배수 모두 False로 전환
            for j in range(2*i, b+1, i):
                prime[j] = False
    for i in range(a, b+1):
        #보다 크고 값이 True면 소수 개수 증가 
        if i > 1 and prime[i] == True:
            total += 1
    print(total)

while (N != 0):
    isPrime(N+1, 2*N)
    N = int(input())