N = int(input())

homes = list(map(int, input().split()))

homes.sort()

# 중앙값일 때 거리 합 최소
print(homes[N // 2 - 1])