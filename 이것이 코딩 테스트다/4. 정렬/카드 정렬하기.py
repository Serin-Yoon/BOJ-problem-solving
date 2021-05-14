import heapq

N = int(input())

cards = []

for i in range(N):
    heapq.heappush(cards, int(input()))

total = 0

# 카드 한 장만 남을 때까지(모두 합쳐질 때까지) 진행
while len(cards) > 1:
    # 첫번째 카드와 두번째 카드 합침
    one = heapq.heappop(cards)
    two = heapq.heappop(cards)
    total += (one + two)
    heapq.heappush(cards, one + two)

print(total)